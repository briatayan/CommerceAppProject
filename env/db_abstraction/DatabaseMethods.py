import sqlite3
from sqlite3 import Error
from os import path
import sys
import re
import datetime

def createConnection(file):
    con = None
    try:
        con = sqlite3.connect(file)
    except Error as e:
        print(e)

    return con

def closeConnection(con):
    con.close()

def insertItems(con, itemList):
    query = "INSERT INTO items (name, price, start_date) VALUES(?,?,?)"
    cur = con.cursor()
    chunkyData = list()
    validData = list()
    specialCharacters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    for chunk in chunkData(itemList):
            cur.execute("BEGIN TRANSACTION")
            for item in chunk:
                name, price, date = item['name'], item['price'], item['start_date']
                if datetime.datetime.strptime(date, "%m/%d/%Y") < datetime.datetime.now():
                    validData.append("Date is before current date: " + date)
                elif len(name) < 4 or len(name) > 10:
                    validData.append("Ignoring item. Name is either less than 4 characters or more than 10. Size: " + str(len(name)))
                elif name[0].isalpha() == False and name[0].isnumeric() == False:
                    validData.append("Ignoring item. First letter is not a digit or a letter: " + name[0])
                elif specialCharacters.search(name) is not None:
                    validData.append("Ignoring item. Contains special characters: " + name)
                else:
                    try:
                        cur.execute(query, (name, price, date))
                        validData.append(True)
                    except Error as e:
                        validData.append("Failed insertion: " + str(e))
            cur.execute("COMMIT")

    return validData

def searchItems(con, keyword, minPrice, maxPrice):
    query = "SELECT name, price, start_date FROM items WHERE "
    minPrice, maxPrice = int(minPrice), int(maxPrice)
    res = list()
    cur = con.cursor()
    if minPrice > maxPrice and maxPrice > 0:
        return res.append("Minimum price is greater than maximum price")
    if minPrice != 0 and not None:
        query = query + "price >= " + str(minPrice) + " AND "
    if maxPrice != 0 and not None:
        query = query + "price <= " + str(maxPrice) + " AND "
    query = query + "LOWER(name) LIKE '%" + keyword.lower() + "%'"
    cur.execute(query)
    res = cur.fetchall()
    if res is None:
        print("res is null", file=sys.stderr)
        return res
    return dbToJsonList(res)

def getAllItems(con):
    query = "SELECT name, price, start_date FROM items"
    cur = con.cursor()
    cur.execute(query)
    res = cur.fetchall()
    if res is None:
        return res
    else:
        return dbToJsonList(res)

def chunkData(itemList, rows=100):
    for i in range(0, len(itemList), rows):
        yield itemList[i:i + rows]

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
