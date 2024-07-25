from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import os
import logging

app = Flask(__name__)
api = Api(app)

# Configure logging to file
logging.basicConfig(
    filename=r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\students_data_loggings.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'  
)

class DataResource(Resource):
    # To insert student data into excel file
    def post(self):
        try:
            json_data = request.get_json()
            logging.info(f"POST request received with data: {json_data}")
            df = pd.DataFrame([json_data])
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\student_data1.xlsx'

            if os.path.exists(excel_file_path):
                existing_df = pd.read_excel(excel_file_path)
                df = pd.concat([existing_df, df], ignore_index=True)
            df.to_excel(excel_file_path, index=False)
            logging.info("Data stored successfully")
            return {'message': 'Data stored successfully'}, 201

        except Exception as e:
            logging.error(f"Error in POST request: {e}")
            return {'error': str(e)}, 500

    # To update particular value
    def put(self):
        try:
            data = request.get_json()
            logging.info(f"PUT request received with data: {data}")
            id = data['student_no']
            new_city = data.get('student', None)
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\student_data1.xlsx'

            if not os.path.exists(excel_file_path):
                logging.warning("Excel file does not exist")
                return {'error': 'Excel file does not exist'}, 404

            df = pd.read_excel(excel_file_path)
            if 'id' not in df.columns:
                logging.warning("ID column does not exist")
                return {'error': 'ID column does not exist'}, 400

            if id not in df['id'].values:
                logging.warning(f"ID {id} not found")
                return {'error': f'ID {id} not found'}, 404

            df.loc[df['id'] == id, 'city'] = new_city
            df.to_excel(excel_file_path, index=False)
            logging.info("Data successfully updated")
            return {'message': 'Data successfully updated'}, 201

        except Exception as e:
            logging.error(f"Error in PUT request: {e}")
            return {'error': str(e)}, 500

    # To completely delete row whose id matches with given Id
    def delete(self):
        try:
            data = request.get_json()
            logging.info(f"DELETE request received with data: {data}")
            id = data['student_no']

            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\student_data1.xlsx'

            if not os.path.exists(excel_file_path):
                logging.warning("Excel file does not exist")
                return {'error': 'Excel file does not exist'}, 404

            df = pd.read_excel(excel_file_path)
            if 'student_no' not in df.columns:
                logging.warning("ID column does   not exist")
                return {'error': 'ID column does not exist'}, 400

            if id not in df['student_no'].values:
                logging.warning(f"ID {id} not found")
                return {'error': f'ID {id} not found'}, 404

            df = df[df['student_no'] != id]
            df.to_excel(excel_file_path, index=False)
            logging.info("Data successfully deleted")
            return {'message': 'Data successfully deleted'}, 200

        except Exception as e:
            logging.error(f"Error in DELETE request: {e}")
            return {'error': str(e)}, 500

api.add_resource(DataResource, '/data')


if __name__ == '__main__':
    app.run(debug=True)
