import hashlib
import json

class TxOutput:
    def __init__(self,output_address,output_amount):
        self.output_address = output_address
        self.output_amount = output_amount


class TxInput:
    def __init__(self,tx_output_id,tx_output_index,signature):
        self.tx_output_id = tx_output_id #refer to UnspentTxOutput
        self.tx_output_index = tx_output_index
        self.signature = signature

class UnspentTxOutput:
    def __init__(self,tx_output_id,tx_output_index, amount, address):
        self.tx_output_id = tx_output_id
        self.tx_output_index = tx_output_index
        self.amount = amount
        self.address = address

class Transaction:
    def __init__(self,hash_id,type,TxOutput,TxInput):
        self.hash_id = hash_id
        self.type = type
        self.TxOutput = TxOutput
        self.TxInput = TxInput

    def get_tx_id(self):
        merge_dict = {**self.TxOutput.__dict__,**self.TxInput.__dict__}
        return hashlib.sha256(json.dumps(merge_dict,sort_keys=True).encode().hexdigest())

    def sign_tx_input(self,private_key):
        signature = private_key.sign(self.hash_id)
        return signature

    def get_unspent_output(self):
        pass
