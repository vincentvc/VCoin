from ecdsa import SigningKey, SECP256k1
import hashlib
import json
from collections import OrderedDict

class Wallet:
    def __init__(self):
        self.public_key = ''
        self.private_key = ''
        self.password_hash = 'P@ssw0rd'

    def generate_wallet(self,password):
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()
        self.password_hash = hashlib.sha512(password.encode()).hexdigest()

    def get_wallet_keys_json(self):
        return json.dumps(OrderedDict({
            'private_key':self.private_key
            ,'public_key':self.public_key
        }))



