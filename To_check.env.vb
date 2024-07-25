import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print(os.getenv('MYSQL_HOST'))
print(os.getenv('MYSQL_USER'))
print(os.getenv('MYSQL_PASSWORD'))
print(os.getenv('MYSQL_DB'))
