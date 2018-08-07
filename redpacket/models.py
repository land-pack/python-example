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

        get_balance_sql = """
            SELECT f_balance as balance
            FROM t_account
            WHERE f_uid=%s AND f_status=0 AND f_balance >= %s
        """
        
        mod_balance_sql = """
            UPDATE t_account
            SET f_balance=f_balance - %s
            WHERE f_uid=%s AND f_status=0 AND f_balance >= %s
        """


        try:
            cursor.execute(get_balance_sql, (f_uid, f_amount))
            d = cursor.fetchone()
            
            cursor.execute(mod_balance_sql, (f_amount, f_uid, f_amount))

            db.commit()    
        except:
            db.rollback()
            print(traceback.format_exc())
            raise
        else:
            return d if d else {}

if __name__ == '__main__':
    d = send_redpacket(12345, 11.000001, 12,1)
    print(d)

    
