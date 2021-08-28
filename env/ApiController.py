from flask import Flask, request, json
import service.CommerceService as service

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/post-one", methods=['POST'])
def postItem():
    # todo: need to implement error handling
    jsonDict = dict(request.get_json())
    jsonItem = jsonDict['posts'][0]
    lastName = service.postItem(jsonItem['name'], jsonItem['price'], jsonItem['start_date'] )
    jsonDict = dict()
    jsonDict['name'] = lastName
    return json.jsonify(jsonDict)

@app.route("/post", methods=['POST'])
def PostItems():
    jsonList = list(request.get_json()['posts'])
    validData = service.postItems(jsonList)
    return json.jsonify(dict({'data' : validData}))

# @app.route("/search?keyword=<keyword>&min_price=<min_price>&max_price=<max_price>", methods=['GET'])
# def searchItems():
#     keyword = request.args.get('keyword')
#     minPrice = request.args.get('min_price')
#     maxPrice = request.args.get('max_price')
#     if (minPrice == None):
#         minPrice = 0
#     # todo: need to implement error handling
#     itemList = service.getItems(keyword, minPrice, maxPrice)
#     return itemList

@app.route("/all-items", methods=['GET'])
def getAllItems():
    itemList = service.getAllItems()
    #logger.info("Request List: \n" + str(itemList))
    return json.jsonify(itemList)
