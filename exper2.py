from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import openpyxl

app = Flask(__name__)
api = Api(app)

class DataResource(Resource):
    def post(self):
        try:
            
            
            json_data = request.get_json()
            print(json_data)
            d = [json_data[i] for i in json_data.keys()]
            df = pd.DataFrame(d)

            ## check that excel is available or not
            ## If yes, read that data
            ## If not, create an excel
            print(df)

            df.to_excel(r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx', index=False)

            return {'message': 'Data stored successfully'}, 201

        except Exception as e:
            return {'error': str(e)}, 500
    def put(self):
        data = request.get_json()
        id= float(data['id'])
        print(id)
        try:
            dfs = pd.read_excel(r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx')
            for key, value in dfs.items():
                if key==id:
                   dfs.city= "Goa"
            dfs.to_excel(r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx', index=False)

            return {'message': 'Data successfully updated'}, 201

        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(DataResource, '/data')

if __name__ == '__main__':
    app.run(debug=True)
