import psycopg2

class Psql:

    def open_conn(self, db_name, host_name, port_num, user_name, passw = None):
        # Establishing the connection
        self.conn = psycopg2.connect(
            database=db_name, 
            user=user_name, 
            password=passw, 
            host=host_name, 
            port= port_num
        )

        # Creating a cursor object using the cursor() method
        self.cursor = self.conn.cursor()
        
    def run_query(self, query, to_commit):
        self.cursor.execute(query)
        if to_commit:
            self.conn.commit()
        return self.cursor.rowcount
    
    def get_result(self, count):
        return self.cursor.fetchmany(count)

    def close_conn(self):
        self.conn.close()
    