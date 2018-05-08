import hashlib
import json

class Block:
	def __init__(self,index,previous_hash,data,timestamp,difficulty,nonce):
		self.index = index
		self.previous_hash = previous_hash
		self.data = data
		self.timestamp = timestamp
		self.difficulty = difficulty
		self.nonce = nonce
		self.hash = hash

	def get_difficulty(self):
		return self.difficulty

