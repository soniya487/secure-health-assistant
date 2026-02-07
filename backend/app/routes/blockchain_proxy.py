from fastapi import APIRouter, Body
import os
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
load_dotenv()

GANACHE = os.environ.get("GANACHE_URL", "http://127.0.0.1:8545")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
ETH_ADDR = os.environ.get("ETH_ADDRESS")
CONTRACT_ADDR = os.environ.get("CHAIN_CONTRACT_ADDRESS")
w3 = Web3(HTTPProvider(GANACHE))
# contract ABI minimal
ABI = [
    {"inputs":[{"internalType":"string","name":"h","type":"string"}],"name":"storeHash","outputs":[],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[],"name":"getLastHash","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},
]
router = APIRouter(prefix="/blockchain", tags=["Blockchain"])
contract = None
if CONTRACT_ADDR:
    contract = w3.eth.contract(address=CONTRACT_ADDR, abi=ABI)

@router.post("/store")
def store_hash(payload: dict = Body(...)):
    global contract
    h = payload.get("record_hash")
    if not contract:
        return {"error":"contract not configured"}
    acct = ETH_ADDR
    nonce = w3.eth.get_transaction_count(acct)
    tx = contract.functions.storeHash(h).buildTransaction({"from":acct,"nonce":nonce,"gas":3000000,"gasPrice":w3.toWei("20","gwei")})
    signed = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return {"tx": tx_hash.hex(), "receipt": dict(receipt)}

@router.get("/last")
def get_last():
    if not contract:
        return {"error":"contract not configured"}
    return {"last_hash": contract.functions.getLastHash().call()}
