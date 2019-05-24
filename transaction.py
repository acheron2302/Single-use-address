#!/usr/bin/python3
# import sys
import rlp
from hexbytes import HexBytes
from web3 import Web3
from ethereum.utils import ecrecover_to_pub
from ethereum.exceptions import InvalidTransaction

class Transaction(rlp.Serializable):
    '''
    Base for transaction
    '''
    def __init__(self, _nonce, _gasPrice, _gasLimit, _to, _value, _init, _v, _r, _s):
        self.nonce = _nonce
        self.gasPrice = _gasPrice
        self.gasLimit = _gasLimit
        self.to = _to
        self.value = _value
        self.init = _init
        self.v = _v
        self.r = _r
        self.s = _s

    def txSigned(self):
        tx = [
            self.nonce,
            self.gasPrice,
            self.gasLimit,
            self.to,
            self.value,
            self.init,
            self.v,
            self.r,
            self.s
        ]
        result = rlp.encode(tx)
        return HexBytes(result)

    def txData(self):
        if self.v == 27 or self.v == 28:
            tx = [
                self.nonce,
                self.gasPrice,
                self.gasLimit,
                self.to,
                self.value,
                self.init
            ]
        else:
            tx = [
                self.nonce,
                self.gasPrice,
                self.gasLimit,
                self.to,
                self.value,
                self.init,
                (self.v - 36) / 2 if (self.v % 2 == 0) else (self.v - 35) / 2, #Return the chain id according to EIP155
                0,
                0
            ]
        return rlp.encode(tx)

    def senderAddress(self):
        code = Web3.sha3(self.txData())
        pub = ecrecover_to_pub(code, self.v, self.r, self.s)

        if pub == b'\x00' * 64:
            raise InvalidTransaction("Invalid signature")

        return Web3.toChecksumAddress("0x" + Web3.sha3(pub).hex()[-40::])
