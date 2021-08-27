import db_abstraction.DatabaseMethods as dbMethods

def createConnection():
    file = "commerce_items.db"
    con = dbMethods.createConnection(file)
    return con

def closeConnection():
    dbMethods.closeConnection()

def postItems(itemList):
    con = createConnection()
    dbMethods.insertItems(con, itemList)
    return True

def postItem(itemName, price):
    con = createConnection()
    dbMethods.insertItem(con, itemName, price)
    closeConnection()
    return True

def searchItems(itemName, minPrice, maxPrice):
    if (minPrice > maxPrice):
        return 400
    return None

def getAllItems():
    con = createConnection()
    itemList = dbMethods.getAllItems(con)
    for item in itemList.values():
        item['start_date'] = convertDate(item['start_date'])
    return itemList

def divideData(data, rows=200):
    for i in data:
        yield data[i:i+1]

def checkName(itemName):
    return None

def convertDate(date):
    formattedDate = date[5:7] + "/" + date[8:10] + "/" + date[0:4]
    return formattedDate

def test():
    print(getAllItems())

#test()
