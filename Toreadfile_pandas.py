import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='details.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
df = pd.read_csv('studentsdata.csv')
logging.info(f"context in file using pandas: {df}")
cities = pd.DataFrame([['rohan', 'IMTECH','PASSED']])
cities.to_csv('studentsdata.csv')