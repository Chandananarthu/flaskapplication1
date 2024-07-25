from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

class DataResource(Resource):
    def post(self):
        json_data = request.get_json()
        
        df2 = pd.read_json(json.dumps(json_data), orient='index')
        
        data_json = df2.to_dict(orient='records')
        data = pd.DataFrame(data_json)  
  
 
        data.to_excel("output.xlsx")
        return jsonify({'data': data_json})
        
# Map the resource to URL
api.add_resource(DataResource, '/data')

if __name__ == '__main__':
    app.run(debug=True)
