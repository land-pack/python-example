import traceback
from db import DB, rdx
from excep import Excep
from algo import generate
from cache import pack_red_packet, pop_one


def send_redpacket(f_uid, f_amount, f_number, f_type, f_min, f_accurate=8):
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
        
        # Insert all redpacket to database
        ins_redp_sql = """
            INSERT INTO t_redpacket_log(
                f_oid, f_sender, f_amount)
                VALUES(%s, %s, %s)
        """
        # Generate redpacket algo ..
        redpacket_values = generate(f_amount, f_number, min_value=f_min, f_type=f_type, f_accurate=f_accurate)


        try:
            cursor.execute(get_balance_sql, (f_uid, f_amount))
            d = cursor.fetchone()

            if not d:
                raise Excep('Invalid account or no enough balance to pay', 410)
            
            cursor.execute(mod_balance_sql, (f_amount, f_uid, f_amount))
            cursor.execute(ins_order_sql, (f_uid, f_amount, f_number, f_type))
            f_oid = cursor.lastrowid

            data = [ (f_oid, f_uid, value) for value in redpacket_values]
            total = cursor.executemany(ins_redp_sql, (data))
            begin_oid = cursor.lastrowid
            print('total', total, 'begin', begin_oid)

            # save oid to cache
            redpacket_oid = list(xrange(begin_oid, begin_oid + total))
            key = pack_red_packet(redpacket_oid, f_oid)

            db.commit()    
        except:
            db.rollback()
            print(traceback.format_exc())
            raise
        else:
            return key


def grab_redpacket(key, uid):

    with DB() as db:
        cursor = db.cursor()

        update_sql = """
            UPDATE t_redpacket_log
            SET f_status=1, f_receiver=%s
            WHERE f_id=%s AND f_status=0
        """

        try:
            oid = pop_one(key)
            print("oid=", oid)
            cursor.execute(update_sql, (uid, oid))
            db.commit()
        except:
            db.rollback()
            print(traceback.format_exc())
            raise
        else:
            return oid

        

if __name__ == '__main__':
    d = send_redpacket(123456, 2.000001, f_number=12,f_type=1, f_min=0.5)
    print(d)

    
