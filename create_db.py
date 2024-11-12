import sqlite3

conn = sqlite3.connect('todo.sqlite')

cursor = conn.cursor()

sql_query = """ CREATE TABLE todo (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    done BOOLEAN,
    priority INTEGER
)"""

cursor.execute(sql_query)