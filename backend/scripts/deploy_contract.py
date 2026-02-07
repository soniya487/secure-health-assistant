import os, json
from solcx import compile_source, install_solc
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
load_dotenv()

install_solc('0.8.17')

GANACHE = os.environ.get("GANACHE_URL","http://127.0.0.1:8545")
w3 = Web3(HTTPProvider(GANACHE))
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
ETH_ADDR = os.environ.get("ETH_ADDRESS")

with open("contracts/SimpleStorage.sol") as f:
    src = f.read()

compiled = compile_source(src, output_values=['abi','bin'])
contract_id, contract_interface = compiled.popitem()
abi = contract_interface['abi']
bytecode = contract_interface['bin']

acct = w3.eth.account.from_key(PRIVATE_KEY)
nonce = w3.eth.get_transaction_count(acct.address)
Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
construct_txn = Contract.constructor().buildTransaction({'from':acct.address,'nonce':nonce,'gas':3000000,'gasPrice':w3.toWei('20','gwei')})
signed = acct.sign_transaction(construct_txn)
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
addr = receipt.contractAddress
print("Contract deployed at:", addr)
# NOTE: set this address in your .env CHAIN_CONTRACT_ADDRESS
