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
            
            # Convert the JSON data into a DataFrame
            df = pd.DataFrame([json_data])

            # Define the Excel file path
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx'

            # Check if the Excel file exists
            if os.path.exists(excel_file_path):
                # If the file exists, read the existing data
                existing_df = pd.read_excel(excel_file_path)
                # Append new data to the existing DataFrame
                df = pd.concat([existing_df, df], ignore_index=True)

            # Write the updated DataFrame to the Excel file
            df.to_excel(excel_file_path, index=False)

            return {'message': 'Data stored successfully'}, 201

        except Exception as e:
            return {'error': str(e)}, 500

    def put(self):
        try:
            data = request.get_json()
            id = data['id']
            new_city = data.get('city', None)

            # Define the Excel file path
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx'

            if not os.path.exists(excel_file_path):
                return {'error': 'Excel file does not exist'}, 404

            # Read the existing data from the Excel file
            df = pd.read_excel(excel_file_path)

            # Check if the 'id' column exists
            if 'id' not in df.columns:
                return {'error': 'ID column does not exist'}, 400

            # Check if the specified ID exists in the DataFrame
            if id not in df['id'].values:
                return {'error': f'ID {id} not found'}, 404

            # Update the city for the specified ID
            df.loc[df['id'] == id, 'city'] = new_city

            # Write the updated DataFrame back to the Excel file
            df.to_excel(excel_file_path, index=False)

            return {'message': 'Data successfully updated'}, 201

        except Exception as e:
            return {'error': str(e)}, 500

    def delete(self):
        try:
            data = request.get_json()
            id = data['id']

            # Define the Excel file path
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx'

            if not os.path.exists(excel_file_path):
                return {'error': 'Excel file does not exist'}, 404

            # Read the existing data from the Excel file
            df = pd.read_excel(excel_file_path)

            # Check if the 'id' column exists
            if 'id' not in df.columns:
                return {'error': 'ID column does not exist'}, 400

            # Check if the specified ID exists in the DataFrame
            if id not in df['id'].values:
                return {'error': f'ID {id} not found'}, 404

            # Delete the row with the specified ID
            df = df[df['id'] != id]

            # Write the updated DataFrame back to the Excel file
            df.to_excel(excel_file_path, index=False)

            return {'message': 'Data successfully deleted'}, 200

        except Exception as e:
            return {'error': str(e)}, 500

    def get(self):
        try:
            course_id = request.args.get('course_id')

            # Define the Excel file path
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx'

            if not os.path.exists(excel_file_path):
                return {'error': 'Excel file does not exist'}, 404

            # Read the existing data from the Excel file
            df = pd.read_excel(excel_file_path)

            # Check if the 'course' column exists
            if 'course' not in df.columns:
                return {'error': 'Course column does not exist'}, 400

            # Filter the DataFrame by the specified course ID
            course_students = df[df['course'] == course_id]

            # Count the number of students in the specified course
            num_students = len(course_students)

            return {'course_id': course_id, 'num_students': num_students}, 200

        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(DataResource, '/data')

if __name__ == '__main__':
    app.run(debug=True)
