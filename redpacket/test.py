"""
It is also possible to create connection objects using the connection.MySQLConection() class:
"""

import MySQLdb

cnx = MySQLdb.connect(user='root', passwd='openmysql',
                                host='127.0.0.1',
                                db='test')

cnx.close()
