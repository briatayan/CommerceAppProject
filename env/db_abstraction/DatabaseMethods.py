import sqlite3
from sqlite3 import Error
import json
from os import path

def createConnection(file):
    con = None
    try:
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

def insertItems(con, itemList):
    cur = con.cursor()
    
    return None

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
    objList = list()
    for res in resList:
        itemName = res[0]
        price = res[1]
        startDate = res[2]
        tempDict = {
            'name' : itemName, 'price' : price, 'start_date' : startDate
        }
        objDict.append(tempDict)
    return objDict

def test():
    con = createConnection('commerce_items.db')
    insertItem(con, "test item 2", 100)
    print(getAllItems(con))
    closeConnection(con)

#test()
