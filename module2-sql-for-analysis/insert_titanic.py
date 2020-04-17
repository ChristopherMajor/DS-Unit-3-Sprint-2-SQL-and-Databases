#goal instert titanic.csv file inot a PG db

#connect to the DB
import psycopg2
import os
from dotenv import load_dotenv
import pandas
from psycopg2.extras import execute_values
import numpy as np
import sqlite3

#this deals with error from np.int54 dtype when inserting into postgres
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

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

#make a table and name columns

table_creation_query = '''
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived integer,
    pclass integer,
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

##insert data into the table. 
#first convert df into a list of tuples
rows_to_insert =list(df.to_records(index=False))


insertion_query = '''
    INSERT INTO passengers (
        survived, pclass, name, gender, age, sib_spouce_count, parent_child_count, fare)
        VALUES %s
    '''

execute_values(cursor, insertion_query, rows_to_insert)

#test a query -- how many rows?
query1 = '''
    SELECT 
	    count(DISTINCT name)
    FROM passengers;
    '''

#execute query

cursor.execute(query1)
result1 = cursor.fetchone()
print(result1)


# cursor.execute('SELECT * from passengers;')

# first_result = cursor.fetchone()
# print(first_result)




#saves our plan into db
cursor.close()
connection.commit()
