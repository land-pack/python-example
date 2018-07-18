import json
from pprint import pprint
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_user = 'my_rpc'
rpc_password= 'my_rpc_password'
rpc_host = '192.168.1.86:9332'

rpc_connection = AuthServiceProxy("http://{}:{}@{}".format(rpc_user, rpc_password, rpc_host))

best_block_hash = rpc_connection.getbestblockhash()

print(best_block_hash)

# batch support : print timestamps of blocks 0 to 90 in 2 RPC round-trips:
commands = [[ "getblockhash", height] for height in range(100)]
block_hashes = rpc_connection.batch_(commands)
blocks = rpc_connection.batch_([[ "getblock", h] for h in block_hashes])
block_times = [block["time"] for block in blocks]
print(len(block_times))







from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging

logging.basicConfig
logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)

rpc_connection = AuthServiceProxy("http://{}:{}@{}".format(rpc_user, rpc_password, rpc_host))
#- getblockchaininfo: blocks, difficulty, chain
#- getnetworkinfo: version, protocolversion, timeoffset, connections, proxy, relayfee, warnings
#- getwalletinfo: balance, keypoololdest, keypoolsize, paytxfee, unlocked_until, walletversion

pprint(rpc_connection.getblockchaininfo())
print('=' * 100)
pprint(rpc_connection.getnetworkinfo())
print('=' * 100)
pprint(rpc_connection.getwalletinfo())
