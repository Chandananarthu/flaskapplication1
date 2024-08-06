from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

class DataResource(Resource):
    def post(self):
        
        json_data = request.get_json()
        df2 = pd.read_json(json.dumps(json_data), orient='index')
        return jsonify({'data': df2})
        
        
# Map the resource to URL
api.add_resource(DataResource, '/data')

if __name__ == '__main__':
    app.run(debug=True)
