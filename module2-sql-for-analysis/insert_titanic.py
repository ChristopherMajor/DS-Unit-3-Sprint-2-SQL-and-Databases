#goal instert titanic.csv file inot a PG db

#connect to the DB
import psycopg2
import os
from dotenv import load_dotenv
import pandas
from psycopg2.extras import execute_values

load_dotenv() #adds contents of .env file

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print(type(connection))

cursor = connection.cursor()
print(type(cursor))

#make a table

table_creation_query = '''
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived integer,
    name varchar NOT NULL,
    gender varchar NOT NULL,
    age float,
    sib_spouce_count integer,
    parent_child_count integer,
    fare float
);
'''
cursor.execute(table_creation_query)

#read csv file and maybe transform the data

df = pandas.read_csv('titanic.csv')
print(df.head())

#insert data into the table. 
#convert df into a list of tuples
rows_to_insert =list(df.to_records(index=False))


insertion_query = "INSERT INTO passengers (survived, pclass, name, gender, age, sib_spouse_count, parent_child_count)"
execute_values(cursor, insertion_query, rows_to_insert)

#saves our plan into db
connection.commit()