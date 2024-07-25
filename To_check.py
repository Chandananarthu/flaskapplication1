import os
from dotenv import load_dotenv

print("Current Working Directory:", os.getcwd())

# Load environment variables from a specific .env file
load_dotenv('mydbms_details1.env')

print(os.getenv('MYSQL_HOST'))
print(os.getenv('MYSQL_USER'))
print(os.getenv('MYSQL_PASSWORD'))
print(os.getenv('MYSQL_DB'))
