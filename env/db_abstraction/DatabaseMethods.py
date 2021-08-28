import sqlite3
from sqlite3 import Error
from os import path

def createConnection(file):
    con = None
    try:
        con = sqlite3.connect(file, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    except Error as e:
        print(e)

    return con

def closeConnection(con):
    con.close()

def insertItem(con, itemName, itemPrice, date):
    cur = con.cursor()
    cur.execute("INSERT INTO items (name, price, start_date) VALUES (?,?,?)", (itemName, str(itemPrice), date))
    lastId = cur.lastrowid
    con.commit()
    return lastId

def insertItems(con, itemList, rows=100):
    cur = con.cursor()
    chunkyData = list()
    counter = 0
    for i in range(0, rows):
        chunkyData.append(chunkData(itemList, counter))

    validData = list()

    for chunk in chunkyData[counter + rows]:

        cur.execute("BEGIN TRANSACTION")

        for name, price, date in chunk:
            isAdded = True # hardcoded
            dataSize.append(isAdded)
            cur.execute("INSERT OR IGNORE INTO items (name, price, start_date) VALUES(?,?,?)", (name, price, date))
        cur.execute("COMMIT")

    return validData

def searchItems(con, itemName, minPrice, maxPrice):
    return None

def getAllItems(con):
    cur = con.cursor()
    cur.execute("SELECT name, price, date(start_date) FROM items")
    res = cur.fetchall()
    if res is None:
        return res
    else:
        return dbToJsonList(res)

def chunkData(itemList, counter):
    chunkyList = list()
    for i in range(0, size(itemList)):
        chunkyList.apppend(i)
        counter = counter + 1
    return tuple(chunkyList, counter)


def dbToJsonList(resList):
    objList = list()
    for res in resList:
        itemName = res[0]
        price = res[1]
        startDate = res[2]
        tempDict = {
            'name' : itemName, 'price' : price, 'start_date' : startDate
        }
        objList.append(tempDict)
    return objList
