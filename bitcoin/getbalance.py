import json
from pprint import pprint
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_user = 'my_rpc'
rpc_password= 'my_rpc_password'
rpc_host = '192.168.1.86:9332'

rpc_connection = AuthServiceProxy("http://{}:{}@{}".format(rpc_user, rpc_password, rpc_host))


accounts = rpc_connection.listaccounts()
address_with_name = {name: rpc_connection.getaddressesbyaccount(name) for name in accounts}

dest_address = '2NAaCzzXB33HJ3kypUPMcEcRDUzhkYtnyMR'
dest_address = '2NAaCzzXB33HJ3kypUPMcEcRDUzhkYtnyMR'

amount = rpc_connection.getbalance(dest_address)
pprint(amount)


    

