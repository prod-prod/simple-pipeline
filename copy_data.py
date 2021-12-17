from modules.my_sql import Mysql
from modules.postgres import Psql


'''
1 connect to postgres - 
2 sel max date from postgres table
3 open connection to mysql
4 select * from sys.orders where date >= max date from postgres
5 get result and insert data in postgres (keep uuid unique)
'''

if __name__=="__main__":
    db_destination = Psql()
    db_destination.open_conn(db_name="postgres", host_name="127.0.0.1", port_num="5432", user_name="postgres",passw="mypassword")
    
    count_match = db_destination.run_query("select max(created) from public.orders", False)   
    max_date = db_destination.get_result(count_match)
    
    extract_query = "select * from sys.orders"

    if max_date[0][0] is not None:
        extract_query += " where created >= '{}'".format(max_date[0][0])
    extract_query += ";"

    db_source = Mysql()
    db_source.open_conn(db_name="mysql", host_name="127.0.0.1", port_num="3306", user_name="root",passw="123456")

    trans_data = db_source.run_query(extract_query, False)
    batch_size = 5

    while trans_data > 0:
        rows = db_source.get_result(batch_size)
        trans_data -= batch_size
        load_query = "insert into public.orders values "
        
        for id, created in rows:
            load_query += "('{}', '{}'),".format(id, created)    
        load_query = load_query[:len(load_query)-1] + " "
        load_query += "on conflict on constraint orders_pkey do nothing;"


        db_destination.run_query(load_query, True)
    

    db_destination.close_conn()
    db_source.close_conn()