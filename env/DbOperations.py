import sqlite3
import os.path
from os import path

def createDb():
    try:
        con = sqlite3.connect('commerce_items.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS items (name VARCHAR(10) PRIMARY KEY, \
            price INTEGER NOT NULL, start_date TIMESTAMP DEFAULT CURRENT_DATE)")
        con.commit()
        con.close()
        print("~~ Created DB successfully ~~")
    except Error as e:
        print("Could not execute create: " + e)

def deleteDb():
    try:
        con = sqlite3.connect('commerce_items.db')
        cur = con.cursor()
        cur.execute("DROP TABLE items")
        con.commit()
        con.close()
        print("~~ Deleted DB successfully ~~")
    except Error as e:
        print("Could not execute delete: " + e)

def restartDb():
    try:
        con = sqlite3.connect('commerce_items.db')
        cur = con.cursor()
        cur.execute("DROP TABLE items")
        cur.execute("CREATE TABLE IF NOT EXISTS items (name VARCHAR(10) PRIMARY KEY, \
            price INTEGER NOT NULL, start_date TIMESTAMP DEFAULT CURRENT_DATE)")
        con.commit()
        con.close()
        print("~~ Restarted DB successfully ~~")
    except Error as e:
        print("Could not execute restart: " + e)
