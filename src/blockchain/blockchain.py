import hashlib
import json
from block.block import *
from config.config import *


class Blockchain:
    def __init__(self):
        self.nodes = set()
        self.blockchain = [self._get_genesis_block()]


    def get_difficulty(self):
        last_block = self.blockchain[-1]
        if last_block.index % DIFFICULTY_ADJUSTMENT_INTERVAL == 0 and last_block.index != 0:
            return self.get_adjusted_difficulty()
        else:
            return last_block.difficulty

    def get_adjusted_difficulty(self):
        last_block = self.blockchain[-1]
        actual_block_time_interval = last_block.timestamp - self.blockchain[-1-DIFFICULTY_ADJUSTMENT_INTERVAL]
        expected_block_time_interval = DIFFICULTY_ADJUSTMENT_INTERVAL*BLOCK_GENERATION_INTERVAL

        if actual_block_time_interval < expected_block_time_interval:
            return last_block.difficulty + 1
        elif actual_block_time_interval > expected_block_time_interval:
            return last_block.difficulty - 1
        else:
            return last_block.difficulty

    def resolve_blockchain_conflicts(self, new_blockchain):
        if self._is_valid_blockchain(new_blockchain):
            pass
        elif self._get_accumlated_difficulty(new_blockchain) > self._get_accumlated_difficulty(self.blockchain):
            self.blockchain = new_blockchain

    def add_block(self,new_block):
        if self._is_valid_new_block(previous_block=self.blockchain[-1],new_block=new_block):
            self.blockchain.append(new_block)
            return True
        else:
            return False

    def find_valid_block(self,block):
        block.nonce = 0
        while True:
            hash = self.get_block_hash(block)
            if self._is_valid_proof_of_work(hash,block.difficulty):
                return block
            block.nonce = block.nonce + 1

    def get_all_blockchain_json(self):
        return json.dumps([block.__dict__ for block in self.blockchain])

    def get_latest_block_json(self):
        return json.dumps(self.blockchain[-1].__dict__)

    def get_block_by_index(self,index):
        return json.dumps(self.blockchain[index].__dict__)

    @classmethod
    def _get_accumlated_difficulty(cls,blockchain):
        accumulated_difficulty = 0
        for block in blockchain:
            accumulated_difficulty = accumulated_difficulty + block.difficulty
        return accumulated_difficulty


    @classmethod
    def _is_valid_blockchain(cls,blockchain):
        block_index = 1
        if blockchain[0].__dict__ != cls._get_genesis_block.__dict__:
            return False
        while block_index < len(blockchain):
            if not cls._is_valid_proof_of_work(blockchain[block_index]):
                return False
            elif not cls._is_valid_new_block(previous_block=blockchain[block_index-1],new_block=blockchain[block_index]):
                return False
        return True


    @classmethod
    def _is_valid_new_block(cls,previous_block,new_block):
        if previous_block.index != new_block.index -1:
            return False
        elif previous_block.hash != new_block.previous_block_hash:
            return False
        elif not cls._is_valid_proof_of_work(new_block):
            return False
        return True


    @staticmethod
    def _is_valid_proof_of_work(hash, difficulty=DIFFICULTY):
        """
        :param hash: In binary
        :param difficulty:
        :return: True if transaction hash pass the difficulty threshold
        """
        required_difficulty_predix = '0' * difficulty
        return hash.startwith(required_difficulty_predix)

    @staticmethod
    def get_block_hash(block):
        return hashlib.sha256(json.dumps(block.__dict__, sort_keys=True).encode()).hexdigest()


    @staticmethod
    def _get_genesis_block():
        return Block(index=0
                     , hash="E6D5041797662ED8D9766D7C284B4C136FDA7CD803C040BB2ECA4B8C3A27A488"
                     , previous_block_hash=""
                     , transaction="ToDoTransaction"
                     , timestamp=1525746201
                     , difficulty=DIFFICULTY
                     , nonce=0)


