import sqlite3
from sqlite3 import Error
import json
from os import path
import InitDb as initDb

def createConnection(file):
    con = None
    try:
        if (not path.exists('commerce_items.db')):
            initDb.createDb()
        con = sqlite3.connect(file)
    except Error as e:
        print(e)

    return con

def closeConnection(con):
    con.close()

def insertItem(con, itemName, itemPrice):
    cur = con.cursor()
    cur.execute("INSERT INTO items (name, price) VALUES ('" + itemName + "', " + str(itemPrice) + ")")
    lastId = cur.lastrowid
    con.commit()
    return lastId

def searchItems(con, itemName, minPrice, maxPrice):
    return None

def getAllItems(con):
    cur = con.cursor()
    cur.execute("SELECT * FROM items")
    res = cur.fetchall()
    if res is None:
        return res
    else:
        return dbToJsonList(res)

def dbToJsonList(resList):
    objDictList = dict()
    objDict = dict()
    for res in resList:
        id = res[0]
        name = res[1]
        price = res[2]
        startDate = res[3]
        tempDict = {
            "name" : name, "price" : price, "start_date" : startDate
        }
        objDict[id] = tempDict
    return objDict

def test():
    con = createConnection('commerce_items.db')
    insertItem(con, "test item 2", 100)
    print(getAllItems(con))
    closeConnection(con)

#test()
