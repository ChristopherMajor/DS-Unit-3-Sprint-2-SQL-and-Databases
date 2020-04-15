import psycopg2
import os
from dotenv import load_dotenv

load_dotenv() #adds contents of .env file

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

print("DB_NAME:", DB_NAME)


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print(type(connection))

cursor = connection.cursor()
print(type(cursor))

cursor.execute('SELECT * from test_table;')

first_result = cursor.fetchone()
print(first_result)

print('------')
all_results = cursor.fetchall()
print(all_results)