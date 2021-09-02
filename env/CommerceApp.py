from flask import Flask, request, json
import service.CommerceService as service
import sys

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/post", methods=['POST'])
def postItems():
    jsonList = request.get_json()
    if list(jsonList) is None or len(jsonList) == 0:
        return json.dumps({'success':False, 'description':'Given list is null or empty.'}), 400, {'ContentType':'application/json'}
    jsonList = list(jsonList['posts'])
    validData = service.postItems(jsonList)
    if validData is None or len(validData) == 0:
        return json.dumps({'success':False, 'description':'Return object is null.'}), 500, {'ContentType':'application/json'}
    return json.jsonify(dict({'valid_data' : validData})), 201

@app.route("/search", methods=['GET'])
def searchItems():
    if request.args.get('keyword') is None:
        return json.dumps({'success':False, 'description': 'Keyword is null.'}), 400, {'ContentType':'application/json'}
    keyword = request.args.get('keyword').lower()
    minPrice = request.args.get('min_price') if (request.args.get('min_price') is not None) else 0
    maxPrice = request.args.get('max_price') if (request.args.get('max_price') is not None) else 0
    itemList = service.searchItems(keyword, minPrice, maxPrice)
    if itemList:
        return json.jsonify(itemList)
    else:
        return json.dumps({'success':False, 'description':'Item does not exist.'}), 200, {'ContentType':'application/json'}

@app.route("/all-items", methods=['GET'])
def getAllItems():
    itemList = service.getAllItems()
    if itemList:
        return json.jsonify(itemList)
    else:
        return json.dumps({'success':False, 'description':'Post list is empty.'}), 200, {'ContentType':'application/json'}
