
from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api 
import logging
   
app = Flask(__name__)  
api = Api(app) 
  

class addition(Resource): 
  
    def get(self): 
        data = request.get_json()
        num1= float(data['num1'])
        num2= float(data['num2'])
    
  
        return jsonify({'sum': num1+num2})
api.add_resource(addition, '/sum') 



  
if __name__ == '__main__': 
    logging.basicConfig(filename='appl.log', filemode='a', 
                        format='%(asctime)s - %(levelname)s - %(message)s', 
                        level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message') 

  
    app.run(debug = True) 
