from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import os

app = Flask(__name__)
api = Api(app)

class DataResource(Resource):
    #To insert student data into excel file
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
    #To Update particular  value 
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
    #to completely delete row whose id matches with given Id
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
    #To get how many students have same course id
    def get(self):
        try:
            course_id = request.args.get('course_id')
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx'

            if not os.path.exists(excel_file_path):
                return {'error': 'Excel file does not exist'}, 404
            df = pd.read_excel(excel_file_path)

        
            if 'course' not in df.columns:
                return {'error': 'Course column does not exist'}, 400

            
            course_students = df[df['course'] == course_id]
            num_students = len(course_students)

            return {'course_id': course_id, 'num_students': num_students}, 200

        except Exception as e:
            return {'error': str(e)}, 500
    #To get info of student that matches the id
    def get_by_id(self):
        try:
            data = request.get_json()
            id = data['id']
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\data.xlsx'

            if not os.path.exists(excel_file_path):
                return {'error': 'Excel file does not exist'}, 404

            df = pd.read_excel(excel_file_path)
            if 'id' not in df.columns:
                return {'error': 'ID column does not exist'}, 400
            student_info = df[df['id'] == id]

            if student_info.empty:
                return {'error': f'ID {id} not found'}, 404

            
            student_info_dict = student_info.to_dict(orient='records')[0]

            return {'student_info': student_info_dict}, 200

        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(DataResource, '/data')
api.add_resource(DataResource, '/data/<int:id>', endpoint='get_by_id')

if __name__ == '__main__':
    app.run(debug=True)
