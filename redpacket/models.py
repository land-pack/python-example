import traceback
from db import DB
from excep import Excep


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
        # Insert a new order to the order table
        ins_order_sql = """
            INSERT INTO t_redpacket_order(
            f_uid, f_amount, f_number, f_type)
            VALUES(%s, %s, %s, %s)
        """

        try:
            cursor.execute(get_balance_sql, (f_uid, f_amount))
            d = cursor.fetchone()

            if not d:
                #raise ....
                raise Excep('Invalid account or no enough balance to pay', 410)
            
            cursor.execute(mod_balance_sql, (f_amount, f_uid, f_amount))
            cursor.execute(ins_order_sql, (f_uid, f_amount, f_number, f_type))

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

    
