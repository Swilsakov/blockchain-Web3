from web3 import Web3


infura_url = "https://mainnet.infura.io/v3/4d4c1fc5f36b4c7d8d643b27d8651138"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0xB3F20d336239A295D3FbEE056Fc304b959E2267e") #Узнать баланс с кошелька Metamask
print(web3.fromWei(balance, 'ether'))
