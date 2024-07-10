from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import logging
from logging.handlers import TimedRotatingFileHandler

app = Flask(__name__)
api = Api(app)

class Addition(Resource):
    def get(self):
        data = request.get_json()
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 + num2
        app.logger.info(f'Sum of {num1} and {num2} calculated: {result}')
        return jsonify({'sum': result})

api.add_resource(Addition, '/sum')


if __name__ == '__main__':
    handler = TimedRotatingFileHandler(filename='appl.log', when='M', interval=1, backupCount=0)
    handler.suffix = '%Y-%m-%d_%H-%M.log'  # Custom suffix format for minute-based rotation
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    # Test log message
    app.logger.info('Testing logging setup.')

    app.run(debug=True)
