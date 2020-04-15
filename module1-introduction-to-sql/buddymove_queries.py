import pandas
import sqlite3
from sqlalchemy import create_engine
#read in local csv
df = pandas.read_csv('buddymove_holidayiq.csv')

engine = create_engine('sqlite:///buddymove_holidayiq.sqlite3')

df.to_sql('review', con = engine, if_exists='append')

engine.execute("SELECT * FROM review").fetchall()

DB_FILEPATH = 'buddymove_holidayiq.sqlite3'
connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

query1 = '''
SELECT 
    count(*)
FROM 
    review
''' 
result1 = cursor.execute(query1).fetchall()
print('how many rows?', result1)