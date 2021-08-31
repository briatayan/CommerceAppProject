import sqlite3
import os.path
from os import path
import argparse

def createDb():
    try:
        con = sqlite3.connect('commerce_items.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS items (name VARCHAR(10) PRIMARY KEY, \
            price INTEGER NOT NULL, start_date TIMESTAMP DEFAULT CURRENT_DATE)")
        con.commit()
        con.close()
        print("~~ Created successfully ~~")
    except Error as e:
        print("Could not execute create: " + e)

def deleteDb():
    try:
        con = sqlite3.connect('commerce_items.db')
        cur = con.cursor()
        cur.execute("DROP TABLE items")
        con.commit()
        con.close()
        print("~~ Deleted successfully ~~")
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
        print("~~ Restarted successfully ~~")
    except Error as e:
        print("Could not execute restart: " + e)

parser = argparse.ArgumentParser(description="Database Methods")
parser.add_argument("op", choices=["create", "delete", "restart"])
args = parser.parse_args()

if args.op == "create":
    createDb()
elif args.op == "delete":
    deleteDb()
elif args.op == "restart":
    restartDb()
