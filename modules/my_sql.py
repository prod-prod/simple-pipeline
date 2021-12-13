import mysql.connector


class Mysql:
 
    def open_conn(self, db_name, host_name, port_num, user_name, passw=None):
        # Establishing the connection
        self.conn = mysql.connector.connect(
            user=user_name, 
            password=passw,
            host=host_name,
            database=db_name,
            port=port_num
        )
        self.cursor = self.conn.cursor()
    
    def run_query(self, query, to_commit):
        self.cursor.execute(query)
        # Make sure data is committed to the database
        if to_commit:
            self.conn.commit()
        self.cursor.fetchall() 
        return self.cursor.rowcount

    def get_result(self, query, count):
        self.cursor.execute(query)
        result = list()
        if count <= 0:
            return result
        for row in self.cursor:
            result.append(row)
            count -= 1
            if count == 0:
                break
        return result

    def close_conn(self):
        #self.cursor.close()
        self.conn.close()
