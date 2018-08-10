"""
It is also possible to create connection objects using the connection.MySQLConection() class:
"""

import traceback
import MySQLdb
import MySQLdb.cursors
import redis
import ConfigParser


rdx = redis.Redis()


class DB(object):
    
    def __init__(self):
        self.port = int(Config.get('mysql', 'port'))
        self.host = Config.get('mysql', 'host')
        self.user = Config.get('mysql', 'user')
        self.passwd = Config.get('mysql', 'passwd')
        self.db = Config.get('mysql', 'db')


    def __enter__(self):
        self.cnx = MySQLdb.connect(user=self.user, passwd=self.passwd,
                                host=self.host,
                                db=self.db,
                                cursorclass=MySQLdb.cursors.DictCursor
                                )
        #self.cursor = self.cnx.cursor(MySQLdb.DictsCursor())
        return self.cnx
    
    def __exit__(self, a, b, c):
        self.cnx.close()

if __name__ == '__main__':
    r.set('ee',123)
    d = r.get('ee')
    print(d)
    r.delete('ee')
