import mysql.connector


class Mysql:
    def __init__(self):
        self.cursor = None
        self.conn = None

    def open_conn(self, db_name, host_name, port_num, user_name, passw=None):
        self.conn = mysql.connector.connect(
            user=user_name,
            password=passw,
            host=host_name,
            database=db_name,
            port=port_num
        )

    def run_query(self, run_query, to_commit):
        if self.cursor is not None:
            self.cursor.close()

        if to_commit:
            self.cursor = self.conn.cursor()
            self.cursor.execute(run_query)
            self.conn.commit()
            self.cursor.close()
            self.cursor = None
            return 0
        else:
            self.cursor = self.conn.cursor(buffered=True)
            self.cursor.execute(run_query)
            return self.cursor.rowcount

    def get_result(self, count):
        # if self.cursor is None or count <= 0:
        #     return []

        result = list()
        while count > 0:
            row = self.cursor.fetchone()

            if row is None:
                self.cursor.close()
                self.cursor = None
                break
            else:
                result.append(row)
                count -= 1

        return result

    def close_conn(self):
        if self.cursor is not None:
            self.cursor.close()

        elif self.conn is not None:
            self.conn.close()
