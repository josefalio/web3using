from web3 import Web3

# Set your Ethereum provider
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY'))

def get_average_gas_price(block_number):
     try:
         block = w3.eth.getBlock(block_number)
         if block:
             gas_limit = block['gasLimit']
             gas_used = block['gasUsed']
             average_gas_price = w3.fromWei(gas_used / gas_limit, 'gwei')
             return average_gas_price
         else:
             return None
     except Exception as e:
         print(f"Error: {e}")
         return None

# Replace 'BLOCK_NUMBER' with the block number for which you want to get the average gas
block_number = 'BLOCK_NUMBER'
average_gas = get_average_gas_price(block_number)

if average_gas is not None:
     print(f"Average Gas Price for Block {block_number}: {average_gas} Gwei")
else:
     print("Failed to retrieve average gas price.")
