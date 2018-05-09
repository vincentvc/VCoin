import hashlib
import json

class Block(object):
	def __init__(self,index,hash,previous_block_hash,transaction,timestamp,difficulty,nonce):
		self.index = index
		self.previous_block_hash = previous_block_hash
		self.transaction = transaction
		self.timestamp = timestamp
		self.difficulty = difficulty
		self.nonce = nonce
		self.hash = hash
