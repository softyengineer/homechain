# https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b

import hashlib as hasher

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
  # __init__ is a special method in Python classes, it is the constructor method for a class
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
    #sha = hasher.sha256()
    sha = hasher.md5()
  def hash_block(self):
    sha.update(str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash))
return sha.hexdigest()