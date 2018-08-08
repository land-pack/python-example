import traceback
from db import DB


def add_test_account(f_uid, f_balance):
    with DB() as db:
        cursor = db.cursor()

        # Insert a new order to the order table
        ins_order_sql = """
            INSERT INTO t_account(
            f_uid, f_balance)
            VALUES(%s, %s)
        """

        try:
            cursor.execute(ins_order_sql, (f_uid, f_balance))
            db.commit()    

        except:
            db.rollback()
            print(traceback.format_exc())
            raise

if __name__ == '__main__':
    add_test_account(123456, 12)

    
