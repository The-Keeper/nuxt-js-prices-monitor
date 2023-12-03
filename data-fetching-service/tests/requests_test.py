import requests
import schedule
from datetime import datetime, timedelta

today = datetime.now().date()
two_years_ago = today - timedelta(days=730)
try:
    response = requests.get(f'https://api.coindesk.com/v1/bpi/historical/close.json?start={two_years_ago.isoformat()}&end={today.isoformat()}')
    response.raise_for_status()        
    data = response.json()
    formatted_tuples = [ (key, 0, value) for key, value in data['bpi'].items() ]
    print(formatted_tuples)
except requests.exceptions.HTTPError as err:
    pass
