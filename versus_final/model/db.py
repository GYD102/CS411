import sqlite3
from sqlite3 import Error
from model.orm import ORM
import os


class DbUtil:
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
            DbUtil.connection = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        finally:
            print('connection success')

    @staticmethod
    def close_connection():
        """ save changes to db and close connection """
        if DbUtil.connection:
            DbUtil.connection.commit()
            DbUtil.connection.close()

    # CREATE TABLE METHODS
    @staticmethod
    def create_table(create_table_sql):
        """
        create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        conn = DbUtil.connection
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    @staticmethod
    def create_user_info_table():
        sql = """
                CREATE TABLE IF NOT EXISTS UserInfo (
                user_id VARCHAR PRIMARY KEY,
                user_name VARCHAR
                );
        """
        DbUtil.create_table(sql)

    @staticmethod
    def create_senator_table():
        sql = """
                CREATE TABLE IF NOT EXISTS Senator (
                    senator_id VARCHAR PRIMARY KEY,
                    image VARCHAR,
                    sen_name VARCHAR,
                    bio VARCHAR
                );
        """
        DbUtil.create_table(sql)

    @staticmethod
    def create_versus_result_table():
        sql = """
            CREATE TABLE IF NOT EXISTS VersusResult (
            versusID INTEGER PRIMARY KEY,
            is_tie bool,
            senatorID1 VARCHAR,
            senatorID2 VARCHAR,
            winnerID VARCHAR,
            user_id VARCHAR,
            FOREIGN KEY (senatorID1) REFERENCES Senator(senator_id),
            FOREIGN KEY (senatorID2) REFERENCES Senator(senator_id),
            FOREIGN KEY (winnerID) REFERENCES Senator(senator_id),
            FOREIGN KEY (user_id) REFERENCES UserInfo(user_id)
            );
        """
        DbUtil.create_table(sql)

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

        cur = DbUtil.connection.cursor()
        cur.execute(sql, [user_id, user_name])

    @staticmethod
    def insert_senator(senator_id, image_url, sen_name, bio):
        sql = """
                INSERT OR REPLACE INTO Senator
                VALUES (?,?,?,?)
        """
        cur = DbUtil.connection.cursor()
        cur.execute(sql, [senator_id, image_url, sen_name, bio])

    @staticmethod
    def insert_versus_result(is_tie, senatorID1, senatorID2, winnerID, user_id):
        sql = """
                INSERT INTO VersusResult (is_tie, senatorID1, senatorID2, winnerID, user_id)
                VALUES (?, ?, ?, ?, ?)
                """
        cur = DbUtil.connection.cursor()
        cur.execute(sql, [is_tie, senatorID1, senatorID2, winnerID, user_id])

    # GET DATA METHODS
    @staticmethod
    def select_user_info(user_id):
        sql = """
                SELECT *
                FROM UserInfo
                WHERE user_id == ?
            """

        cur = DbUtil.connection.cursor()
        cur.execute(sql, [user_id])

        return cur.fetchone()

    @staticmethod
    def select_senator(senator_id):
        sql = """
                SELECT *
                FROM Senator
                WHERE senator_id == ?
              """

        cur = DbUtil.connection.cursor()
        cur.execute(sql, [senator_id])

        return cur.fetchone()

    @staticmethod
    def select_versus_results(user_id):
        sql = """
              SELECT *
              FROM VersusResult
              WHERE user_id == ?
        """

        cur = DbUtil.connection.cursor()
        cur.execute(sql, [user_id])

        return cur.fetchall()

    @staticmethod
    def run_sql_select(sql):
        cur = DbUtil.connection.cursor()
        cur.execute(sql)

        return cur.fetchall()

    # ETC.
    @staticmethod
    def get_supported_senators():
        return {
            'Lamar Alexander': 'A000360',
            'Tammy Baldwin': 'B001230',
            'John Barrasso': 'B001261',
            'Michael Bennet': 'B001267',
            'Richard Blumenthal': 'B001277',
            'Roy Blunt': 'B000575',
            'Joe Donnelly': 'D000607',
            'Richard Durbin': 'D000563',
            'Michael Enzi': 'E000285',
            'Charles Schumer': 'S000148',
            'Elizabeth Warren': 'W000817',
            'Steve Daines': 'D000618',
            'Joni Ernst': 'E000295',
            'Tammy Duckworth': 'D000622'
        }

    @staticmethod
    def get_questions_scores_topics():

        # question to score; where
        questions = ['Do you support abortion?',
                     'Do you believe there should be more constraints on the process of purchasing a gun?',
                     'Do you support international intervention?',
                     'Do you support the US continuing NSA surveillance of its allies?',
                     'Should the US accept refugees?',
                     'Should the tax rate for corporations increase?',
                     'Do you support the Patient Protection and Affordable Care Act (Obamacare)?',
                     'Do you support the legalization of same sex marriage?']

        # score corresponds to positive sentiment response
        affirmative_scores = [-1, 1, -1, -1, 1, 1, 1, 1]

        topics = ['Abortion',
                  'Firearms and explosives',
                  'Refugees,asylum,displaced persons',
                  'Intelligence activities,surveillance,classified information',
                  'Immigration status and procedures',
                  'Tax administration and collection,taxpayers',
                  'Health care coverage and access',
                  'Sex,gender,sexual orientation discrimination']

        return questions, affirmative_scores, topics

    @staticmethod
    def get_senator_object(senator_id):
        senator = ORM.map_senator(DbUtil.select_senator(senator_id))
        return senator

    @staticmethod
    def get_versus_results_objects(versus_results_tuples):
        arr = []
        for tup in versus_results_tuples:
            arr.append(ORM.map_versus_result(tup))
        return arr


def test():
    DbUtil.create_connection()

    if DbUtil.connection:

        DbUtil.create_user_info_table()
        DbUtil.create_senator_table()
        DbUtil.create_versus_result_table()

        # print("TEST INSERTS: ")
        # SQLiteUtil.insert_senator('test', 'test_url', 'test_name', 'test_bio')
        # SQLiteUtil.insert_user_info('test_user_id', 'test_user_name')
        # SQLiteUtil.insert_versus_result(True, 'test_senator_id', 'test_senator_id2', 'test_winner_id', 'test_user_id')
        #
        # print(SQLiteUtil.select_user_info('test_user_id'))
        # print(SQLiteUtil.select_senator('test'))
        # print(SQLiteUtil.select_versus_results('test_user_id'))
        # print()

        print("PRINTING ALL ROWS")
        print("USER INFOS:", DbUtil.run_sql_select("SELECT * FROM UserInfo"))
        print("SENATORS:", DbUtil.run_sql_select("SELECT * FROM Senator"))
        print("RESULTS:", DbUtil.run_sql_select("SELECT * FROM VersusResult"))

    else:
        print("Error! cannot create the database connection.")

    DbUtil.close_connection()


if __name__ == '__main__':
    test()
