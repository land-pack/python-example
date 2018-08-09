import json
from pprint import pprint
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_user = 'my_rpc'
rpc_password= 'my_rpc_password'
rpc_host = '192.168.1.86:9332'

rpc_connection = AuthServiceProxy("http://{}:{}@{}".format(rpc_user, rpc_password, rpc_host))

best_block_hash = rpc_connection.getbestblockhash()

accounts = rpc_connection.listaccounts()
address_with_name = {name: rpc_connection.getaddressesbyaccount(name) for name in accounts}

print(accounts)
pprint(address_with_name)


dest_address = raw_input("Please input the address what you want to send ")
currency = raw_input("Please input the number of currency ") or 0

if currency == 0:
    print("Currency couldn't be less or equal 0")
    print("Currency are required more 0")
else:
    rpc_connection.sendtoaddress(dest_address, int(currency))

