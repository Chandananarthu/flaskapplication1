import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_restful import Resource, Api
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv('mydbms_details1.env')

app = Flask(__name__)
api = Api(app)

# Initialize MySQL with direct environment variable access
mysql = MySQL()
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
mysql.init_app(app)

def setup_logging():
    handler = TimedRotatingFileHandler('sql_log.log', when='midnight',interval=1, backupCount=3)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)


class StudentResource(Resource):
    def post(self):
        if request.is_json:
            data = request.get_json()
            student_no = data.get('student_no')
            student_name = data.get('student_name')
            phone_no = data.get('phone_no')
            email = data.get('email')
            guide = data.get('guide')

            if not all([student_no, student_name, phone_no, email, guide]):
                app.logger.error('Missing data in request')
                return {'error': 'Missing data'}, 400

            try:
                cur = mysql.connection.cursor()

                # Create table if it doesn't exist
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS Students (
                        student_no INT PRIMARY KEY,
                        student_name VARCHAR(100),
                        phone_no VARCHAR(15),
                        email VARCHAR(100),
                        guide VARCHAR(100)
                    )
                ''')
                mysql.connection.commit()

                # Insert student details into the table
                cur.execute("INSERT INTO Students(student_no, student_name, phone_no, email, guide) VALUES (%s, %s, %s, %s, %s)", 
                            (student_no, student_name, phone_no, email, guide))
                mysql.connection.commit()
                cur.close()
                app.logger.info(f'Student {student_no} added successfully')
        
                return {'message': 'Student added successfully'}, 201
            
            
            except Exception as e:
                app.logger.error(f'Unexpected error: {str(e)}')
                return {'error': 'An unexpected error occurred: ' + str(e)}, 500
        else:
            app.logger.error('Request must be JSON')
            return {'error': 'Request must be JSON'}, 400

    def put(self):
        if request.is_json:
            data = request.get_json()
            student_no = data.get('student_no')
            field = data.get('field')
            value = data.get('value')

            if not all([student_no, field, value]):
                app.logger.error('Missing data in update request')
                return {'error': 'Missing data'}, 400

            if field not in ['student_name', 'phone_no', 'email', 'guide']:
                app.logger.error(f'Invalid field: {field}')
                return {'error': 'Invalid field'}, 400

            try:
                cur = mysql.connection.cursor()

                # Update the specific field
                query = f"UPDATE Students SET {field} = %s WHERE student_no = %s"
                cur.execute(query, (value, student_no))
                mysql.connection.commit()

                if cur.rowcount == 0:
                    app.logger.warning(f'No student found with student_no: {student_no}')
                    return {'error': 'Student not found'}, 404

                cur.close()
                app.logger.info(f'Student {student_no} updated successfully')
                return {'message': 'Student updated successfully'}, 200

            
            except Exception as e:
                app.logger.error(f'Unexpected error: {str(e)}')
                return {'error': 'An unexpected error occurred: ' + str(e)}, 500
        else:
            app.logger.error('Request must be JSON')
            return {'error': 'Request must be JSON'}, 400

    def delete(self):
        if request.is_json:
            data = request.get_json()
            student_no = data.get('student_no')

            if not student_no:
                app.logger.error('Missing student_no in delete request')
                return {'error': 'Missing student_no'}, 400

            try:
                cur = mysql.connection.cursor()

                # Delete the student record
                cur.execute("DELETE FROM Students WHERE student_no = %s", (student_no,))
                mysql.connection.commit()

                if cur.rowcount == 0:
                    app.logger.warning(f'No student found with student_no: {student_no}')
                    return {'error': 'Student not found'}, 404

                cur.close()
                app.logger.info(f'Student {student_no} deleted successfully')
                return {'message': 'Student deleted successfully'}, 200

            
            except Exception as e:
                app.logger.error(f'Unexpected error: {str(e)}')
                return {'error': 'An unexpected error occurred: ' + str(e)}, 500
        else:
            app.logger.error('Request must be JSON')
            return {'error': 'Request must be JSON'}, 400
    def get(self):
        if request.is_json:
            data=request.get_json()
            student_no=data.get('student_no')
            
            if not student_no:
                app.logger.error("Missing student_no value in get request")
                return {'error': 'Mising student_no value'}, 400
            try:
                cur=mysql.connection.cursor()
                cur.execute("select *from students where student_no=%s",(student_no,))
                result = cur.fetchone()  # Use fetchone() to get a single record
                cur.close()

                if result:
                    student_data = {
                        'student_no': result[0],
                        'student_name': result[1],
                        'phone_no': result[2],
                        'email': result[3],
                        'guide': result[4]
                    }
                    app.logger.info(f'Student {student_no} fetched successfully')
                    return jsonify(student_data)
                else:
                    app.logger.warning(f'No student found with student_no: {student_no}')
                    return {'error': 'Student not found'}, 404
            
            
            except Exception as e:
                app.logger.error(f'Unexpected error: {str(e)}')
                return {'error': 'An unexpected error occurred: ' + str(e)}, 500
        else:
            app.logger.error('Request must be JSON')
            return {'error': 'Request must be JSON'}, 400

class StudentDetails(Resource):
    def get(self):
        if request.is_json:
            data=request.get_json()
            guide=data.get('guide')
            
            if not guide:
                app.logger.error("guide value is not provided in request object")
                return {'error':'guide value should be provided to get result to query'}, 400
            try:
                cur=mysql.connection.cursor()
                cur.execute("select count(*) from students where guide = %s",(guide,))
                result=cur.fetchone()
                count=result[0]
                cur.close()
                app.logger.info(f'Count of student {result} fetched successfully')
                return {'count': count}, 200

            except Exception as e:
                app.logger.error(f'unexpected error occured: {str(e)}')
                return {'error': 'An unexpected error occurred: ' + str(e)}, 500

        else:
            app.logger.error('Request object is not json it must json')
            return {'error':'Request object must be JSON'}, 400
# Adding resources to API
api.add_resource(StudentResource, '/students')
api.add_resource(StudentDetails, '/count_is' )

if __name__ == '__main__':
    setup_logging()
    app.run(debug=True)
