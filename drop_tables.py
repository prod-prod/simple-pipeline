from modules.my_sql import Mysql
from modules.postgres import Psql


if __name__ == "__main__":
    db_mysql = Mysql()
    db_mysql.open_conn(db_name="mysql", host_name="127.0.0.1",
                       port_num="3306", user_name="root", passw="123456")

    db_mysql.run_query("""
    drop table if exists sys.orders;
    """, True)

    db_mysql.close_conn()

    db_psql = Psql()
    db_psql.open_conn(db_name="postgres", host_name="127.0.0.1",
                      port_num="5432", user_name="postgres", passw="mypassword")

    db_psql.run_query("""
    drop table if exists public.orders;
    """, True)

    db_psql.close_conn()
