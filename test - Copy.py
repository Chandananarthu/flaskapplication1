from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api 

   
app = Flask(__name__)  
api = Api(app) 
  

class Square(Resource): 
  
    def get(self): 
        data = request.get_json()
        num1= float(data['num1'])
        num2= float(data['num2'])
    
  
        return jsonify({'sum': num1+num2})
api.add_resource(Square, '/sum') 



  
if __name__ == '__main__': 
  
    app.run(debug = True) 
