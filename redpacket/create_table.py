"""
It is also possible to create connection objects using the connection.MySQLConection() class:
"""

import MySQLdb

cnx = MySQLdb.connect(user='root', passwd='openmysql',
                                host='127.0.0.1',
                                db='test')
cur = cnx.cursor()

clean_account_sql = "DROP TABLE IF EXISTS `t_account`"
clean_order_sql = "DROP TABLE IF EXISTS `t_redpacket_order`"
clean_log_sql = "DROP TABLE IF EXISTS `t_redpacket_log`"
clean_journal_log_sql = "DROP TABLE IF EXISTS `t_cash_log`"

create_account_sql = """
    CREATE TABLE t_account(
        f_id BIGINT NOT NULL AUTO_INCREMENT,
        f_uid BIGINT NOT NULL UNIQUE,
        f_balance DECIMAL(16,8),
        f_status int NOT NULL DEFAULT 0,
        f_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
        PRIMARY KEY (f_id))
"""

create_journal_sql = """
    CREATE TABLE t_cash_log(
        f_id BIGINT NOT NULL AUTO_INCREMENT,
        f_uid BIGINT NOT NULL,
        f_oid BIGINT NOT NULL DEFAULT 0,
        f_inout INT NOT NULL DEFAULT 0,
        f_amount DECIMAL(16,8),
        f_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
        PRIMARY KEY (f_id))
"""


create_order_sql = """
    CREATE TABLE t_redpacket_order(
        f_id BIGINT NOT NULL AUTO_INCREMENT,
        f_uid BIGINT NOT NULL,
        f_amount DECIMAL(16, 8) NOT NULL,
        f_unspent DECIMAL(16, 8) NOT NULL DEFAULT 0,
        f_number INT NOT NULL COMMENT 'number of redpacket',
        f_coin INT NOT NULL DEFAULT 0,
        f_accurate INT NOT NULL DEFAULT 0,
        f_type int NOT NULL DEFAULT 0 COMMENT '`0` Normally, `1` random; (1 ~ 1+ mean algor ID',
        f_status int NOT NULL DEFAULT 0 COMMENT '`0` New; `1` received but no open; `2` received & opened; `3` rollback to sender',
        f_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),

        PRIMARY KEY(f_id)
        )
    """

create_log_sql = """
    CREATE TABLE t_redpacket_log(
        f_id BIGINT NOT NULL AUTO_INCREMENT,
        f_oid BIGINT,
        f_sender BIGINT NOT NULL,
        f_receiver BIGINT,
        f_amount DECIMAL(16, 8) NOT NULL,
        f_status INT NOT NULL DEFAULT 0,
        f_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
        unique index agd(f_oid, f_receiver),
        PRIMARY KEY(f_id))
"""

cur.execute(clean_account_sql)
cur.execute(clean_order_sql)
cur.execute(clean_log_sql)
cur.execute(clean_journal_log_sql)

cur.execute(create_log_sql)
cur.execute(create_order_sql)
cur.execute(create_account_sql)
cur.execute(create_journal_sql)

cnx.commit()
cnx.close()
