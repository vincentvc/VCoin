class Block:
	def __init__(self,index,hash,previous_hash,data,timestamp,difficulty,nonce,mined_by,block_reward):
		self.index = index;
		self.hash = hash;
		self.previous_hash = previous_hash;
		self.data = data;
		self.timestamp = timestamp;
		self.difficulty = difficulty;
		self.nonce = nonce;
		self.mined_by = mined_by;
		self.block_reward = block_reward;
