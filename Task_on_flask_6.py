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

class Student(Resource):
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

    # To update a particular value
    def put(self):
        try:
            data = request.get_json()
            logging.info(f"PUT request received with data: {data}")
            student_no = data.get('student_no')
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\student_data1.xlsx'

            if not os.path.exists(excel_file_path):
                logging.warning("Excel file does not exist")
                return {'error': 'Excel file does not exist'}, 404

            df = pd.read_excel(excel_file_path)

            if 'student_no' not in df.columns:
                logging.warning("Student number column does not exist")
                return {'error': 'Student number column does not exist'}, 400

            if student_no not in df['student_no'].values:
                logging.warning(f"Student number {student_no} not found")
                return {'error': f'Student number {student_no} not found'}, 404

            for key, value in data.items():
                if key in df.columns and key != 'student_no':
                    df.loc[df['student_no'] == student_no, key] = value

            df.to_excel(excel_file_path, index=False)
            logging.info("Data successfully updated")
            return {'message': 'Data successfully updated'}, 201

        except Exception as e:
            logging.error(f"Error in PUT request: {e}")
            return {'error': str(e)}, 500
    # To completely delete the row whose id matches with the given Id
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
                logging.warning("ID column does not exist")
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

    # To get how many students have the same course ID
    def get(self):
        try:
            data = request.get_json()
            course_id = data.get('course')
            logging.info(f"GET request received for course_id: {course_id}")
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\student_data1.xlsx'

            if not os.path.exists(excel_file_path):
                logging.warning("Excel file does not exist")
                return {'error': 'Excel file does not exist'}, 404

            df = pd.read_excel(excel_file_path)
            if 'course' not in df.columns:
                logging.warning("Course column does not exist")
                return {'error': 'Course column does not exist'}, 400

            course_students = df[df['course'] == course_id]
            num_students = len(course_students)
            logging.info(f"Number of students in course {course_id}: {num_students}")
            return {'course_id': course_id, 'num_students': num_students}, 200

        except Exception as e:
            logging.error(f"Error in GET request: {e}")
            return {'error': str(e)}, 500
        
        
class StudentDetails(Resource):
    # To get info of a student that matches the ID
    def get(self):
        try:
            data = request.get_json()
            logging.info(f"GET request received with data: {data}")
            id = data['student_no']
            excel_file_path = r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\student_data1.xlsx'

            if not os.path.exists(excel_file_path):
                logging.warning("Excel file does not exist")
                return {'error': 'Excel file does not exist'}, 404

            df = pd.read_excel(excel_file_path)
            if 'student_no' not in df.columns:
                logging.warning("ID column does not exist")
                return {'error': 'ID column does not exist'}, 400

            student_info = df[df['student_no'] == id]
            if student_info.empty:
                logging.warning(f"ID {id} not found")
                return {'error': f'ID {id} not found'}, 404

            student_info_dict = student_info.to_dict(orient='records')[0]
            logging.info(f"Student info retrieved for ID {id}: {student_info_dict}")
            return {'student_info': student_info_dict}, 200

        except Exception as e:
            logging.error(f"Error in GET by ID request: {e}")
            return {'error': str(e)}, 500

api.add_resource(Student, '/data')
api.add_resource(StudentDetails, '/student')

if __name__ == '__main__':
    app.run(debug=True)
