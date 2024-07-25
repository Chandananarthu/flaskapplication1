from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import os
import logging
import mysql.connector
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)

# Configure logging to file
logging.basicConfig(
    filename=r'D:\OneDrive - Quadratic Insights Pvt Ltd\projects\data\students_data_loggings.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'  
    )

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Nchandana123@'
app.config['MYSQL_DB'] = 'dataBase'
 
mysql = MySQL(app)
cursor = mysql.connection.cursor()
class Student(Resource):
    # To insert student data into excel file
    def post(self):
        try:
            json_data = request.get_json()
            logging.info(f"POST request received with data: {json_data}")
            df = pd.DataFrame([json_data])
            A=df['name']
            B=df['id']
            # creating table 
            studentRecord = """CREATE TABLE STUDENT (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""
  
            # table created
            cursor.execute(studentRecord) 
            sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
            VALUES (%s, %s)"
            val = (A,B)
            cursor.execute(sql, val)
            mysql.connection.commit()
   
            # disconnecting from server
            cursor.close()
            logging.info("Data stored successfully")
            return {'message': 'Data stored successfully'}, 201

        except Exception as e:
            logging.error(f"Error in POST request: {e}")
            return {'error': str(e)}, 500
if __name__ == '__main__':
    app.run(debug=True)