from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import os

app = Flask(__name__)
api = Api(app)

class DataResource(Resource):
    def post(self):
        try:
            json_data = request.get_json()
            print(json_data)
            
            df = pd.DataFrame([json_data])

            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx'

            if os.path.exists(excel_file_path):
                existing_df = pd.read_excel(excel_file_path)
                df = pd.concat([existing_df, df], ignore_index=True)

            df.to_excel(excel_file_path, index=False)

            return {'message': 'Data stored successfully'}, 201

        except Exception as e:
            return {'error': str(e)}, 500

    def put(self):
        try:
            data = request.get_json()
            id = data['id']
            new_city = data.get('city', None)

            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx'

            if not os.path.exists(excel_file_path):
                return {'error': 'Excel file does not exist'}, 404

            df = pd.read_excel(excel_file_path)

            if 'id' not in df.columns:
                return {'error': 'ID column does not exist'}, 400

            if id not in df['id'].values:
                return {'error': f'ID {id} not found'}, 404

            df.loc[df['id'] == id, 'city'] = new_city

            df.to_excel(excel_file_path, index=False)

            return {'message': 'Data successfully updated'}, 201

        except Exception as e:
            return {'error': str(e)}, 500

    def delete(self):
        try:
            data = request.get_json()
            id = data['id']

            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx'

            if not os.path.exists(excel_file_path):
                return {'error': 'Excel file does not exist'}, 404

            df = pd.read_excel(excel_file_path)

            if 'id' not in df.columns:
                return {'error': 'ID column does not exist'}, 400

    
            if id not in df['id'].values:
                return {'error': f'ID {id} not found'}, 404

            df = df[df['id'] != id]

            df.to_excel(excel_file_path, index=False)

            return {'message': 'Data successfully deleted'}, 200

        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(DataResource, '/data')

if __name__ == '__main__':
    app.run(debug=True)
