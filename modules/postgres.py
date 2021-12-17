import psycopg2

class Psql:
    def __init__(self):
        self.cursor = None
        self.conn = None

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
        # self.cursor = self.conn.cursor()
        
    def run_query(self, run_query, to_commit):
        if self.cursor is not None:
            self.cursor.close()

        if to_commit:
            self.cursor = self.conn.cursor()
            self.cursor.execute(run_query)
            self.conn.commit()
            self.cursor.close()
            self.cursor = None

        else:
            self.cursor = self.conn.cursor()
            self.cursor.execute(run_query)
            return self.cursor.rowcount

    
    def get_result(self, count):
        return self.cursor.fetchmany(count)


    def close_conn(self):
        if self.cursor is not None:
            self.cursor.close()

        elif self.conn is not None:
            self.conn.close()

    