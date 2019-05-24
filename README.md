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

The result from the txSigned is:
```0xf911d5808504a817c8008312a5418080b91182608060405234801561001057600080fd5b50611162806100206000396000f3fe608060405234801561001057600080fd5b50600436106100a5576000357c010000000000000000000000000000000000000000000000000000000090048063a41e7d5111610078578063a41e7d511461028d578063aabbb8ca146102fa578063b705676514610388578063f712f3e81461040d576100a5565b806329965a1d146100aa5780633d584063146101185780635df8122f1461019c57806365ba36c114610200575b600080fd5b610116600480360360608110156100c057600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610492565b005b61015a6004803603602081101561012e57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506108f0565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6101fe600480360360408110156101b257600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506109f5565b005b6102776004803603602081101561021657600080fd5b810190808035906020019064010000000081111561023357600080fd5b82018360208201111561024557600080fd5b8035906020019184600183028401116401000000008311171561026757600080fd5b9091929391929390505050610bb7565b6040518082815260200191505060405180910390f35b6102f8600480360360408110156102a357600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080357bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19169060200190929190505050610bf1565b005b6103466004803603604081101561031057600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610d5f565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6103f36004803603604081101561039e57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080357bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19169060200190929190505050610e4d565b604051808215151515815260200191505060405180910390f35b6104786004803603604081101561042357600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080357bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19169060200190929190505050610f3a565b604051808215151515815260200191505060405180910390f35b60008073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff16146104cd57836104cf565b335b90503373ffffffffffffffffffffffffffffffffffffffff166104f1826108f0565b73ffffffffffffffffffffffffffffffffffffffff1614151561057c576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600f8152602001807f4e6f7420746865206d616e61676572000000000000000000000000000000000081525060200191505060405180910390fd5b610585836110b5565b1515156105fa576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601a8152602001807f4d757374206e6f7420626520616e20455243313635206861736800000000000081525060200191505060405180910390fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415801561066357503373ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff1614155b156108015760405160200180807f455243313832305f4143434550545f4d414749430000000000000000000000008152506014019050604051602081830303815290604052805190602001208273ffffffffffffffffffffffffffffffffffffffff1663249cb3fa85846040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808381526020018273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019250505060206040518083038186803b15801561075057600080fd5b505afa158015610764573d6000803e3d6000fd5b505050506040513d602081101561077a57600080fd5b8101908080519060200190929190505050141515610800576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260208152602001807f446f6573206e6f7420696d706c656d656e742074686520696e7465726661636581525060200191505060405180910390fd5b5b816000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600085815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508173ffffffffffffffffffffffffffffffffffffffff16838273ffffffffffffffffffffffffffffffffffffffff167f93baa6efbd2244243bfee6ce4cfdd1d04fc4c0e9a786abd3a41313bd352db15360405160405180910390a450505050565b60008073ffffffffffffffffffffffffffffffffffffffff16600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16141561098d578190506109f0565b600160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1690505b919050565b3373ffffffffffffffffffffffffffffffffffffffff16610a15836108f0565b73ffffffffffffffffffffffffffffffffffffffff16141515610aa0576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600f8152602001807f4e6f7420746865206d616e61676572000000000000000000000000000000000081525060200191505060405180910390fd5b8173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff1614610ad95780610adc565b60005b600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff167f605c2dbf762e5f7d60a546d42e7205dcb1b011ebc62a61736a57c9089d3a435060405160405180910390a35050565b6000828260405160200180838380828437808301925050509250505060405160208183030381529060405280519060200120905092915050565b610bfb8282610e4d565b610c06576000610c08565b815b6000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000837bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506001600260008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000837bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19167bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916815260200190815260200160002060006101000a81548160ff0219169083151502179055505050565b600080600073ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff1614610d9c5783610d9e565b335b9050610da9836110b5565b15610dd3576000839050610dbd8282610f3a565b610dc8576000610dca565b815b92505050610e47565b6000808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600084815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169150505b92915050565b6000806000610e7f856301ffc9a77c0100000000000000000000000000000000000000000000000000000000026110e5565b80925081935050506000821480610e965750600081145b15610ea657600092505050610f34565b610ed38563ffffffff7c0100000000000000000000000000000000000000000000000000000000026110e5565b80925081935050506000821480610eeb575060008114155b15610efb57600092505050610f34565b610f0585856110e5565b8092508193505050600182148015610f1d5750600181145b15610f2d57600192505050610f34565b6000925050505b92915050565b6000600260008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000837bffffffffffffffffffffffffffffffffffffffffffffffffffffffff19167bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916815260200190815260200160002060009054906101000a900460ff161515610fef57610fe88383610e4d565b90506110af565b8273ffffffffffffffffffffffffffffffffffffffff166000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000847bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161490505b92915050565b6000806001027bffffffffffffffffffffffffffffffffffffffffffffffffffffffff6001028316149050919050565b60008060006301ffc9a77c010000000000000000000000000000000000000000000000000000000002905060405181815284600482015260208160248389617530fa9350805192505050925092905056fea165627a7a72305820af300f82226f561046bf7c7f0a8c424054fcbc3c037efcad8a2b8896d7bbd03100291ba01820182018201820182018201820182018201820182018201820182018201820a01820182018201820182018201820182018201820182018201820182018201820 ```

The result from the senderAddress is:
```0x47AdA9D30bB2655204E7E8C4494627A6dEF588E0```

# Note
You must run this script on default ganache test net because web3 need to take the gasPrice from a chain.

