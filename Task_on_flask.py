from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def post(self):
        data = request.get_json()  # Get JSON data from POST request
        if data:
            try:
                with open('students.json', 'a') as f:
                    json.dump(data, f)  # Write JSON data to file
                    f.write('\n')  # Add newline for each entry
                    pd.read_json("students.json").to_excel("output.xlsx")
                return {'message': 'Student information saved successfully'}, 201
            except Exception as e:
                return {'error': str(e)}, 500
        else:
            return {'error': 'No input data provided'}, 400


api.add_resource(Student, '/student')

if __name__ == '__main__':
    app.run(debug=True)
