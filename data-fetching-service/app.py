import psycopg2
import threading

# a dummy non-active event for testing, so app with wait here forever
dummy_event = threading.Event()
dummy_event.wait() 


conn = psycopg2.connect(host="postgres", dbname="price", user="admin", password="admin")