import psycopg2
import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd
import json

from sqlalchemy import create_engine, select

#connecting to postgre 
load_dotenv() #adds contents of .env file

RPG_DB_NAME = os.getenv("DB_NAME")
RPG_DB_USER = os.getenv("DB_USER")
RPG_DB_PASSWORD = os.getenv("DB_PASSWORD")
RPG_DB_HOST = os.getenv("DB_HOST")

pg_connection = psycopg2.connect(dbname=RPG_DB_NAME, user=RPG_DB_USER,
                        password=RPG_DB_PASSWORD, host=RPG_DB_HOST)

pg_cursor = pg_connection.cursor()

#connecting to sqlite rpg db
DB_FILEPATH = "rpg_db.sqlite3"
sql_conn = sqlite3.connect(DB_FILEPATH)
sql_cursor = sql_conn.cursor()

def refresh():
    command = "DROP TABLE IF EXISTS charactercreator_character"
    pg_cursor.execute(command)

refresh()

# #cols = 
# sql_cursor.execute('''
#     SELECT *
#     FROM charactercreator_character
#     ''').fetchall()

create_char_table = \
    """CREATE TABLE charactercreator_character(
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT);"""

pg_cursor.execute(create_char_table)

chars=sql_cursor.execute('''
    SELECT * FROM charactercreator_character
    ''').fetchall()

#print(chars)
#exit()

for c in chars:
    insert_char = \
    '''
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES'''+str(c[1:])+';'
    

    pg_cursor.execute(insert_char)


##EXAMPLE QUERY--
# cursor.execute('SELECT * from passengers;')

# first_result = cursor.fetchone()
# print(first_result)

query1 = '''
    SELECT
        count(name)
    FROM charactercreator_character
    ;'''


pg_cursor.execute(query1)
first_result = pg_cursor.fetchall()
print(first_result)

pg_cursor.close()
pg_connection.commit()






