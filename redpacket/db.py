"""
It is also possible to create connection objects using the connection.MySQLConection() class:
"""

import traceback
import MySQLdb
import MySQLdb.cursors


class DB(object):
    
    def __init__(self):
        # config here
        pass

    def __enter__(self):
        self.cnx = MySQLdb.connect(user='root', passwd='openmysql',
                                host='127.0.0.1',
                                db='test',
                                cursorclass=MySQLdb.cursors.DictCursor
                                )
        #self.cursor = self.cnx.cursor(MySQLdb.DictsCursor())
        return self.cnx
    
    def __exit__(self, a, b, c):
        self.cnx.close()


