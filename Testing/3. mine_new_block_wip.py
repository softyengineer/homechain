# ...blockchain
# ...Block class definition
# https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d
import indicator
import getpass
user = getpass.getuser()

miner_address = user

# PiZeroWest is allowed to change the properties of the living room lights
#      "li-lr-wt-bs": brightness,
#      "ls-lm-wt-on": on,



# Add in:
# 1. Call from when change in variable
# 2. Pass in new variable values (brightness /100, off/on)
# 3. Add other variables to blocks (state of other devices e.g. movement sensors, brightness, etc.)
# 4. Add block to chain, if previous block(s) are new (arrive at the same time) then the block's are added in incrementing values,
  # from a parameter which is calculated from: ((999999999) - hash(block))


def proof_of_work(last_proof): #3.
  # Create a variable that we will use to find
  # our next proof of work
  #incrementor = last_proof + 1
  indicator = difference.has_changed
  # import difference
  # Keep incrementing the incrementor until
  # it's equal to a number divisible by 9
  # and the proof of work of the previous
  # block in the chain
  #while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
    #incrementor += 1
	while not (indicator.has_changed);
# wait until there is an input from a variable
  # Once that number is found,
  # we can return it as a proof
  # of our work
  return indicator

@node.route('/mine', methods = ['GET'])
def mine():
  # Get the last proof of work
  last_block = blockchain[len(blockchain) - 1]
  last_proof = last_block.data['proof']
  # Find the proof of work for
  # the current block being mined
  # Note: The program will hang here until a new
  #       proof of work is found
  proof = proof_of_work(last_proof)
  # Once we find a valid proof of work,
  # we know we can mine a block so 
  # we reward the miner by adding a transaction
  this_nodes_transactions.append(
    { "from": "network", "to": miner_address, "amount": 1 }
  )
  # Now we can gather the data needed
  # to create the new block
##  new_block_data = {
##    "proof-of-work": proof,
##    "transactions": list(this_nodes_transactions)
##  }

  new_block_data_ = {
      "proof": proof,
      "ls-lm-wt-bs": brightness,
      "ls-lm-wt-on": on,
      # Also include previous data
      "ls-lm-et-bs": lslmetbs,
      "ls-lm-et-on": lslmeton,
    }

# proof = proof-of-work
# ls-lm-wt-bs = lights-livingroom-west-brightness
# ls-lm-wt-on = lights-livingroom-west-on,

  
  new_block_index = last_block.index + 1
  new_block_timestamp = this_timestamp = date.datetime.now()
  last_block_hash = last_block.hash
  # Empty transaction list
  this_nodes_transactions[:] = []
  # Now create the
  # new block!
  mined_block = Block(
    new_block_index,
    new_block_timestamp,
    new_block_data,
    last_block_hash
  )
  blockchain.append(mined_block)
  # Let the client know we mined a block
  return json.dumps({
      "index": new_block_index,
      "timestamp": str(new_block_timestamp),
      "data": new_block_data,
      "hash": last_block_hash
}) + "\n"
