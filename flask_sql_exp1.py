import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_restful import Resource, Api
import MySQLdb

app = Flask(__name__)
api = Api(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Nchandana123@'
app.config['MYSQL_DB'] = 'MyDBstudent'

mysql = MySQL(app)

def setup_logging():
    handler = RotatingFileHandler('sql_log.log', maxBytes=10000, backupCount=3)
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
            
            except MySQLdb.Error as e:
                app.logger.error(f'MySQL error: {str(e)}')
                return {'error': str(e)}, 500
            except Exception as e:
                app.logger.error(f'Unexpected error: {str(e)}')
                return {'error': 'An unexpected error occurred: ' + str(e)}, 500
        else:
            app.logger.error('Request must be JSON')
            return {'error': 'Request must be JSON'}, 400

# Adding resources to API
api.add_resource(StudentResource, '/students')

if __name__ == '__main__':
    setup_logging()
    app.run(debug=True)
