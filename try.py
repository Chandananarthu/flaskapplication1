from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import logging

app = Flask(__name__)  
api = Api(app)

def setup_logging():
    logging.basicConfig(
        filename='appl.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        datefmt='%d-%b-%y %H:%M:%S'
    )
    logging.debug('Logging setup complete')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

class Addition(Resource):
    def get(self):
        setup_logging()
        try:
            data = request.get_json()
            num1 = float(data['num1'])
            num2 = float(data['num2'])
            result = num1 + num2
            logging.info(f'Addition performed: {num1} + {num2} = {result}')
            return jsonify({'sum': result})
        except ValueError as e:
            logging.error(f'Invalid value provided: {e}')
            return jsonify({'error': f'Invalid value provided: {e}'}), 400
        

api.add_resource(Addition, '/sum')

if __name__ == '__main__':
    app.run(debug=True)
