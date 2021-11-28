from web3 import Web3
import json

# Транзакции - отправка эфира
# https://www.trufflesuite.com/ganache
# Скачать и установить

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
# print(web3.isConnected())


account_1 = "0xf45b45466df862C039010AFc9741455DA46a277D"
account_2 = "0xC2c965582938d06A90C1f7C6fA62b5961eC9E338"

private_key = "94d65d4717a1f3c7d16a426ef81ca9eb9637e4e896d84a1a0f077e0c5f967448"

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)
# build a transaction
tx = {
    "nonce" : nonce,
    "to" : account_2,
    "value" : web3.toWei(1, 'ether'),
    "gas" : 2000000,
    "gasPrice" : web3.toWei('50', 'gwei')

}
# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# print(tx_hash) # После запуска проверить ganache там произвелась транзакция 1го эфира
print(web3.toHex(tx_hash))
# get tansaction hash