import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling


class MySQLCursorDict(mysql.connector.cursor.MySQLCursor):
    def _row_to_python(self, rowdata, desc=None):
        row = super(MySQLCursorDict, self)._row_to_python(rowdata, desc)
        if row:
            return dict(zip(self.column_names, row))
        return None



connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                                              pool_size=5,
                                                              pool_reset_session=True,
                                                              host='localhost',
                                                              database='david_db',
                                                              user='root',
                                                              password='openmysql')

print ("Printing connection pool properties ")
print("Connection Pool Name - ", connection_pool.pool_name)
print("Connection Pool Size - ", connection_pool.pool_size)



# Get connection object from a pool
class DB(object):
    def __enter__(self):
        connection_object = connection_pool.get_connection()
        self.connection_object = connection_object
        return connection_object 

    def __exit__(self, Type, value, traceback):
        if self.connection_object.is_connected():
            self.connection_object.close()


def test_sql_version():
    with DB() as db:
        cursor = db.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to - ", record)


if __name__ == '__main__':
    test_sql_version()
