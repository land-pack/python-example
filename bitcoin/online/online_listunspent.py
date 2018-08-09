import json
from pprint import pprint
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_user = 'my_rpc'
rpc_password= 'my_rpc_password'
rpc_host = '192.168.1.86:9332'

rpc_connection = AuthServiceProxy("http://{}:{}@{}".format(rpc_user, rpc_password, rpc_host))

addr = '1JiJJbX7Y6LFANTwd8Kjvge1bN7ySzN9zy'

print(addr, rpc_connection.listunspent(0))
print(rpc_connection.getblocks())
    

