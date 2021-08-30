import db_abstraction.DatabaseMethods as dbMethods
import datetime

def createConnection():
    file = "commerce_items.db"
    con = dbMethods.createConnection(file)
    return con

def closeConnection(con):
    dbMethods.closeConnection(con)

def postItems(itemList):
    con = createConnection()
    validData = dbMethods.insertItems(con, itemList)
    return validData

def searchItems(itemName, minPrice, maxPrice):
    con = createConnection()
    itemList = dbMethods.searchItems(con, itemName, minPrice, maxPrice)
    closeConnection(con)
    return itemList

def getAllItems():
    con = createConnection()
    itemList = dbMethods.getAllItems(con)
    return itemList
