# Single-use-address
Generate rawtx with web3py

The tx.py is the example where i use ERC1820Register contract to test the transaction: https://github.com/0xjac/ERC1820/blob/master/contracts/ERC1820Registry.sol, compile using solc 0.5.3.

The deploy.py is to deploy the contract to the local test chain.
## Transaction.py

The class will give out the sender address, raw tx, txData. Init code is as follow
```
nonce: The nonce of from address (if for single use address MUST set it to 0)
gasPrice: the gas price of the chain (use web3.eth.gasPrice to get back the gas price)
gasLimit: the gas limit of the chain (use web3.eth.estimateGas(data: [contract_bytecode]) to get back estimate gas)
to: the address u want to send to
value: the value to send
data(init): the data to send
v: v of the eliptic curve signature (MAY use 27 and 28 for all chain compatibility)
r: r of the eliptic curve signature
s: s of the eliptic curve signature
```

### Object txData 
Give back the transaction signing data
### Object txSigned 
Give back the raw transaction with the signature from v, r, s you have input
### Object senderAddress 
Give back the address which will make the transaction

### Example
From the tx.py, i have already input these parameter ```nonce: 0```, ```gasPrice: web3.eth.gasPrice (2 * 10 ** 9) ```, ```gasLimit: web3.eth.estimateGas(data: [ERC1820 byte code])```, ```to: address(0) ```, ```value: 0 ```, ```data: [ERC1820 byte code] ```, ```v: 27 ```, ```r: 0x1820182018201820182018201820182018201820182018201820182018201820 ```, ```s: 0x1820182018201820182018201820182018201820182018201820182018201820 ```.

The result from the senderAddress is:
```0x47AdA9D30bB2655204E7E8C4494627A6dEF588E0```

# Note
You must run this script on default ganache test net because web3 need to take the gasPrice from a chain.

