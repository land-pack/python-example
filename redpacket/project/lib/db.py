"""
It is also possible to create connection objects using the connection.MySQLConection() class:
"""

import traceback
import MySQLdb
import MySQLdb.cursors
import redis


rdx = redis.Redis()


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

if __name__ == '__main__':
    r.set('ee',123)
    d = r.get('ee')
    print(d)
    r.delete('ee')
