# https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b

import datetime as date

def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
return Block(0, date.datetime.now(), "Genesis HomeBlock", "0")
