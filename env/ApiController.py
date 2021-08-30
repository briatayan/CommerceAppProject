from flask import Flask, request, json
import service.CommerceService as service
import sys

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/post", methods=['POST'])
def PostItems():
    jsonList = list(request.get_json()['posts'])
    if jsonList is None:
        return json.dumps({'success':False, 'description':'Given list is null'}), 400, {'ContentType':'application/json'}
    validData = service.postItems(jsonList)
    if validData is None:
        return json.dumps({'success':False, 'description':'Return object is null'}), 500, {'ContentType':'application/json'}
    return json.jsonify(dict({'data' : validData})), 201

@app.route("/search", methods=['GET'])
def searchItems():
    if request.args is None:
        return json.dumps({'success':False, 'description':'All parameters are null'}), 400, {'ContentType':'application/json'}
    keyword = request.args.get('keyword').lower()
    minPrice = request.args.get('min_price')
    maxPrice = request.args.get('max_price')
    # todo: need to implement error handling
    itemList = service.searchItems(keyword, minPrice, maxPrice)
    return json.jsonify(itemList)

@app.route("/all-items", methods=['GET'])
def getAllItems():
    itemList = service.getAllItems()
    return json.jsonify(itemList)
