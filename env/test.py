import unittest
import json
import requests
import DbOperations as dbOps

class Test(unittest.TestCase):

    def setUp(self):
        dbOps.restartDb()

    def test_post_cases(self):
        url = 'http://localhost:5000/'
        data = {
              "posts": [
                {
                  "name": "skb45",
                  "price": 30702,
                  "start_date": "08/30/2022"
                },
                {
                  "name": "LDupSy",
                  "price": 49456,
                  "start_date": "08/21/2021" # invalid, date is before curr date
                },
                {
                  "name": "@IYt4S9",
                  "price": 53612,
                  "start_date": "11/06/2021" # invalid, name starts with spec char
                },
                {
                  "name": "L6k",
                  "price": 23407,
                  "start_date": "10/30/2021" # invalid, name too short
                },
                {
                  "name": "uYoe@d4",
                  "price": 78624,
                  "start_date": "11/03/2021" # invalid, contains spec chars
                },
                {
                  "name": "skb45",
                  "price": 30702,
                  "start_date": "08/30/2022" # invalid, duplicate of existing post
                }
              ]
            }
        res = requests.post(url + 'post', json=data)
        validDataList = res.json()['valid_data']
        self.assertEqual(validDataList[0], True)
        self.assertEqual(validDataList[1], "Ignoring item. Date is before current date: 08/21/2021")
        self.assertEqual(validDataList[2], "Ignoring item. First letter is not a digit or a letter: @")
        self.assertEqual(validDataList[3], "Ignoring item. Name is either less than 4 characters or more than 10. Size: 3")
        self.assertEqual(validDataList[4], "Ignoring item. Contains special characters: uYoe@d4")
        self.assertEqual(validDataList[5], "Failed insertion: UNIQUE constraint failed: items.name")

    def test_post_cases_invalid_request_null(self):
        url = 'http://localhost:5000/'
        data = {}
        res = requests.post(url + 'post', json=data)
        res = json.loads(res.text)
        self.assertEqual(res.get('success'), False)

    def test_post_cases_invalid_request_empty_list(self):
        url = 'http://localhost:5000/'
        data = {"posts" : []}
        res = requests.post(url + 'post', json=data)
        res = json.loads(res.text)
        self.assertEqual(res.get('success'), False)

    def test_search_cases(self):
        url = 'http://localhost:5000/'
        data = {
               "posts": [
                {
                  "name": "skab45",
                  "price": 30702,
                  "start_date": "08/30/2022"
                },
                {
                  "name": "LDupSy",
                  "price": 49456,
                  "start_date": "08/21/2022"
                }
              ]
            }
        requests.post(url + 'post', json=data)
        res = requests.get(url + 'search?keyword=ab&min_price=30000&max_price=35000')
        self.assertEqual(json.loads(res.text)[0]['name'], 'skab45' )
        res = requests.get(url + 'search?keyword=s&min_price=0&max_price=0')
        self.assertEqual(len(json.loads(res.text)), 2)
        res = requests.get(url + 'search?keyword=ab&min_price=0')
        self.assertEqual(json.loads(res.text)[0]['name'], 'skab45' )
        res = requests.get(url + 'search?keyword=du')
        self.assertEqual(json.loads(res.text)[0]['name'], 'LDupSy' )
        res = requests.get(url + 'search?keyword=SKA')
        self.assertEqual(json.loads(res.text)[0]['name'], 'skab45' )

    def test_search_no_keyword(self):
        url = 'http://localhost:5000/'
        data = {
               "posts": [
                {
                  "name": "skab45",
                  "price": 30702,
                  "start_date": "08/30/2022"
                },
                {
                  "name": "LDupSy",
                  "price": 49456,
                  "start_date": "08/21/2022"
                }
              ]
            }
        requests.post(url + 'post', json=data)
        res = requests.get(url + "search")
        res = json.loads(res.text)
        self.assertEqual(res.get('success'), False)

if __name__ == '__main__':
    unittest.main()
    #dbOps.restartDb()
