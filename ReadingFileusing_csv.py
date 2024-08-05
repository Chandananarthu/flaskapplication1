import csv
import logging

# Configure logging
logging.basicConfig(filename='details.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    with open('studentsdata.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for line in csvFile:
            logging.info(f"Read line: {line}")

except Exception as e:
    logging.error(f"Failed to read CSV file: {e}")
