import sqlite3
from sqlite3 import Error
import os


class SQLiteUtil:
    connection = None

    # CONNECTION METHODS
    @staticmethod
    def create_connection():
        """
        create a database connection to a SQLite database
        """
        dir_path = os.path.dirname(os.path.abspath(__file__))
        db_file = dir_path + '/py_sqlite.db'
        try:
            SQLiteUtil.connection = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        finally:
            print('connection success')

    @staticmethod
    def close_connection():
        """ save changes to db and close connection """
        if SQLiteUtil.connection:
            SQLiteUtil.connection.commit()
            SQLiteUtil.connection.close()

    # CREATE TABLE METHODS
    @staticmethod
    def create_table(create_table_sql):
        """
        create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        conn = SQLiteUtil.connection
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    @staticmethod
    def create_user_info_table():
        sql = """
                CREATE TABLE IF NOT EXISTS UserInfo (
                user_id VARCHAR(255) PRIMARY KEY,
                user_name VARCHAR(255)
                );
        """
        SQLiteUtil.create_table(sql)

    @staticmethod
    def create_senator_table():
        sql = """
                CREATE TABLE IF NOT EXISTS Senator (
                    senator_id VARCHAR(255) PRIMARY KEY,
                    image VARCHAR(255),
                    sen_name VARCHAR(255),
                    bio VARCHAR(255)
                );
        """
        SQLiteUtil.create_table(sql)

    @staticmethod
    def create_versus_result_table():
        sql = """
            CREATE TABLE IF NOT EXISTS VersusResult (
            versusID INTEGER PRIMARY KEY,
            is_tie bool,
            senatorID1 VARCHAR(255),
            senatorID2 VARCHAR(255),
            winnerID VARCHAR(255),
            user_id VARCHAR(255),
            FOREIGN KEY (senatorID1) REFERENCES Senator(senator_id),
            FOREIGN KEY (senatorID2) REFERENCES Senator(senator_id),
            FOREIGN KEY (winnerID) REFERENCES Senator(senator_id),
            FOREIGN KEY (user_id) REFERENCES UserInfo(user_id)
            );
        """
        SQLiteUtil.create_table(sql)

    # INSERT ROW METHODS
    @staticmethod
    def insert_user_info(user_id, user_name):
        """
        :param vals:
        """
        sql = """
              INSERT OR REPLACE INTO UserInfo
              VALUES (?,?)
              """

        cur = SQLiteUtil.connection.cursor()
        cur.execute(sql, [user_id, user_name])

    @staticmethod
    def insert_senator(senator_id, image_url, sen_name, bio):
        sql = """
                INSERT OR REPLACE INTO Senator
                VALUES (?,?,?,?)
        """
        cur = SQLiteUtil.connection.cursor()
        cur.execute(sql, [senator_id, image_url, sen_name, bio])

    @staticmethod
    def insert_versus_result(is_tie, senatorID1, senatorID2, winnerID, user_id):
        sql = """
                INSERT INTO VersusResult (is_tie, senatorID1, senatorID2, winnerID, user_id)
                VALUES (?, ?, ?, ?, ?)
                """
        cur = SQLiteUtil.connection.cursor()
        cur.execute(sql, [is_tie, senatorID1, senatorID2, winnerID, user_id])

    @staticmethod
    def select_user_info(user_id):
        sql = """
                SELECT *
                FROM UserInfo
                WHERE user_id == ?
            """

        cur = SQLiteUtil.connection.cursor()
        cur.execute(sql, [user_id])

        return cur.fetchone()

    @staticmethod
    def select_senator(senator_id):
        sql = """
                SELECT *
                FROM Senator
                WHERE senator_id == ?
              """

        cur = SQLiteUtil.connection.cursor()
        cur.execute(sql, [senator_id])

        return cur.fetchone()

    @staticmethod
    def select_versus_results(user_id):
        sql = """
              SELECT *
              FROM VersusResult
              WHERE user_id == ?
        """

        cur = SQLiteUtil.connection.cursor()
        cur.execute(sql, [user_id])

        return cur.fetchall()

    @staticmethod
    def run_sql_select(sql):
        cur = SQLiteUtil.connection.cursor()
        cur.execute(sql)

        return cur.fetchall()


def test():
    SQLiteUtil.create_connection()

    if SQLiteUtil.connection:

        SQLiteUtil.create_user_info_table()
        SQLiteUtil.create_senator_table()
        SQLiteUtil.create_versus_result_table()

        SQLiteUtil.insert_senator('test', 'test_url', 'test_name', 'test_bio')
        SQLiteUtil.insert_user_info('test_user_id', 'test_user_name')
        SQLiteUtil.insert_versus_result(True, 'test_senator_id', 'test_senator_id2', 'test_winner_id', 'test_user_id')

        print(SQLiteUtil.select_user_info('test_user_id'))
        print(SQLiteUtil.select_senator('test'))
        print(SQLiteUtil.select_versus_results('test_user_id'))

        print(SQLiteUtil.run_sql_select("SELECT * FROM UserInfo"))

    else:
        print("Error! cannot create the database connection.")

    SQLiteUtil.close_connection()


if __name__ == '__main__':
    test()
