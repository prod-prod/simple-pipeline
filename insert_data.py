from modules.my_sql import Mysql
import uuid
import time


query_template =  "insert into sys.orders values ('{}', current_timestamp());"

if __name__ == "__main__":
    db = Mysql()
    db.open_conn(db_name="mysql", host_name="127.0.0.1", port_num="3306", user_name="root",passw="123456")
    for i in range(10):
        id = str(uuid.uuid1())    
        db.run_query(query_template.format(id), True)
        time.sleep(1)

    db.close_conn()
    