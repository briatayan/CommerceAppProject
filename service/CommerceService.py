import db_abstraction.DatabaseMethods as dbMethods

def createConnection():
    file = "commerce_items.db"
    con = dbMethods.createConnection()
    return con

def closeConnection():
    dbMethods.closeConnection()

def postItem(name, price):
    con = createConnection()
    lastId = dbMethods.insertItem(con, name, price)
    closeConnection()
    return lastId

def convertDate(date):
    formattedDate = date[5:6] + "/" + date[8:9] + "/" + date[0:3]
    return formattedDate

def test():
    print(convertDate('2001-08-23'))

test()
