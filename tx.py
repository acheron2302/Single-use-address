#!/usr/bin/python3

from web3 import Web3
from hexbytes import HexBytes
import json
from transaction import Transaction

contract = json.loads(open('./erc1820/build/contracts/ERC1820Registry.json').read())
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

contract_abi = contract['abi']
contract_bytecode = HexBytes(contract['bytecode'])

gas_limit = web3.eth.estimateGas({'data': contract_bytecode})
gas_price = web3.eth.gasPrice

v = 27
r = 0x1820182018201820182018201820182018201820182018201820182018201820
s = 0x1820182018201820182018201820182018201820182018201820182018201820

X = Transaction(0, gas_price, gas_limit, '', 0, contract_bytecode, v, r, s)
result = X.txSigned()
print(result.hex())
print('')
print(X.senderAddress())
