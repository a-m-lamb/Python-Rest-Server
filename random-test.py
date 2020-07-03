import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import requests
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask_jsonpify import jsonify
from json import dumps

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('[key json email]', scope)
client = gspread.authorize(creds)
sqlStudyGuide = client.open("[name of spreasheet]").sheet1

app = Flask(__name__)
api = Api(app)
CORS(app)
@app.route("/")

class SQLFlashCards(Resource):
    def get(self):
        content = sqlStudyGuide.get_all_records()
        return jsonify(content)
        # whenever user navigate to ‘server-url/employees’ then ‘get()’
        #  function of ‘Employees’ class shall be executed and its result 
        #  shall be returned to user.
        
api.add_resource(SQLFlashCards, "/sql") # Route_1
if __name__ == '__main__':
     app.run(port=5002)

