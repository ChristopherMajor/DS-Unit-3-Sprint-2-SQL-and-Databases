"""
"""

from psycopg2 import connect

from .config import load_config

_pg = load_config("postgres")


class PgHelper:
    """Helper class for postgres interactions
    """

    _questions = []
    _queries = []

    def __init__(self, credentials: dict = _pg.PG_CFG) -> None:

        self._credentials = credentials

        self.establish_connection

    def register_queries(self, queries: dict):
        """Register queries with the helper
        
        Arguments:
            queries {dict} -- dictionary of queries where the question 
            is the key and the query needed to answer is the value

            (ex. {"The sky is what color?": "SELECT color FROM sky})
        """

        for key, value in queries:
            self._questions.append(key)
            self._queries.append(value)

    def refresh(self):
        """Drops table if it exists"""

        command = "DROP TABLE IF EXISTS " + _pg.TABLE_NAME
        self.cur.execute(command)

    @property
    def establish_connection(self):
        """establishes a connection with the postgres database
        """
        c = self._credentials

        conn = connect(
            dbname=c["name"], user=c["username"], password=c["password"], host=c["host"]
        )

        cur = conn.cursor()

        return conn, cur

    def close_connection(self):
        self.cur.close()
        self.conn.commit()

    def create_table(self):
        """migrate the rpg character table from sqlite3 to postgres
        """
        table_creation = f'CREATE_TABLE {_pg.TABLE_NAME}({_pg.SCHEMA});'
        conn, cur = self.establish_connection

        cur.execute(table_creation)



print(PgHelper(credentials=load_config("postgres").PG_CFG)._credentials)

