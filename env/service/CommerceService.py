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

def postItem(itemName, price, date):
    con = createConnection()
    dbMethods.insertItem(con, itemName, price, date)
    closeConnection(con)
    return True

# def searchItems(itemName, minPrice, maxPrice):
#     if (minPrice > maxPrice):
#         return 400
#     return None

def getAllItems():
    con = createConnection()
    itemList = dbMethods.getAllItems(con)
    #logger.info("DB List: \n" + str(itemList))
    return itemList

# def checkName(itemName):
#     return None

def test():
    print(getAllItems())

#test()
