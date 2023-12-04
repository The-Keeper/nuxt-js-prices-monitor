import psycopg2
import psycopg2.extras as extras

import threading
import requests
import schedule
from datetime import datetime, timedelta

import time

import logging
#logging.basicConfig(level = logging.INFO)

conn = psycopg2.connect(host="postgres", dbname="price", user="admin", password="admin")
# Create a cursor
conn.autocommit = True
cur = conn.cursor()

def parse_response():
    pass

def populate_job():
    # Count rows in a table
    cur.execute("SELECT COUNT(*) FROM currency")
    row_count: int = cur.fetchone()[0]
    if row_count == 0:
        cur.execute("INSERT INTO currency VALUES ( 0, 'USD', 'USD' )")

    cur.execute("SELECT COUNT(*) FROM price_data")
    row_count: int = cur.fetchone()[0]
    if row_count == 0:
        today = datetime.now().date()
        two_years_ago = today - timedelta(days=730)
        try:
            response = requests.get(f'https://api.coindesk.com/v1/bpi/historical/close.json?start={two_years_ago.isoformat()}&end={today.isoformat()}')
            response.raise_for_status()        
            data = response.json()
            formatted_tuples = [ (key, 0, value) for key, value in data['bpi'].items() ]
            extras.execute_values(cur, "INSERT INTO price_data (time, currency_id, price) VALUES %s", formatted_tuples)

            logging.info("Database populated.") 
            return schedule.CancelJob
        except requests.exceptions.HTTPError as err:
            pass
    else:
        return schedule.CancelJob

schedule.every(5).seconds.do(populate_job)

while True:
    schedule.run_pending()
    time.sleep(1)
