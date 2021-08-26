import sqlite3
import os.path
from os import path

def createDb():
    con = sqlite3.connect('commerce_items.db')
    cur = con.cursor()

    cur.execute(''' CREATE TABLE IF NOT EXISTS items (id INTEGER NOT NULL PRIMARY KEY, \
        name VARCHAR(10) NOT NULL, price INTEGER NOT NULL, \
        start_date DATE DEFAULT CURRENT_DATE) ''')

    con.commit()

    con.close()

def main():
    if (not path.exists('commerce_items.db')):
        createDb()
    else:
        print("DB already exists.")

main()
