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


def send_redpacket(f_uid, f_amount, f_number, f_type):
    with DB() as db:
        cursor = db.cursor()

        sql = """
            SELECT f_balance as balance
            FROM t_account
            WHERE f_uid=%s AND f_status=0
        """

        try:
            cursor.execute(sql, (f_uid, ))
            d = cursor.fetchone()
        except:
            db.rollback()
            print(traceback.format_exc())
            raise
        else:
            return d if d else {}

if __name__ == '__main__':
    d = send_redpacket('12', 12, 12,1)
    print(d)

    
