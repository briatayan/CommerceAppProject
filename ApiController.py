from flask import Flask, request, json
import service.CommerceService as service

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/post", methods=['POST'])
def postItem():

    # todo: need to implement error handling
    jsonDict = dict(request.get_json())
    lastId = service.postItem(jsonDict)
    return lastId



@app.route("/search?keyword=<keyword>&min_price=<min_price>&max_price=<max_price>", methods=['GET'])
def searchItems():
    keyword = request.args.get('keyword')
    minPrice = request.args.get('min_price')
    maxPrice = request.args.get('max_price')

    if (minPrice == None):
        minPrice = 0

    # todo: need to implement error handling
    itemList = service.getItems(keyword, minPrice, maxPrice)
    return itemList
