import hashlib
import json
from .Block import Block
from time import time

class Blockchain:
    def __init__(self):
        self.transactions = []
        self.nodes = set()
        self.blockchain = [self.get_genesis_block()]


    def get_latest_difficulty(self):
        #TODO
        return

    def verify_signature(self,sender_address,signature,trasaction):
        return 0


    def verify_block(self,block):
        return 0

    def create_block(self,previous_hash,nonce):
        """
        :param previous_hash:
        :param nonce:
        Add a new block after verifying the new block
        """

        block = Block(id=len(self.blockchain)+1
                      ,timestamp=time()
                      ,nonce=nonce
                      ,previous_hash=previous_hash
                      )
    def get_block_hash(self,block):
        """
        :param block:
        :return: String: block hash

        Hash block with ordered parameter
        """
        return hashlib.sha256(json.dumps(block.__dict__, sort_keys=True).encode()).hexdigest()




    @staticmethod
    def _get_genesis_block():
        return Block(0,"E6D5041797662ED8D9766D7C284B4C136FDA7CD803C040BB2ECA4B8C3A27A488","","Genesis Block",1525746201,0,0)

