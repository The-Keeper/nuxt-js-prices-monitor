import psycopg2
import psycopg2.extras as extras

conn = psycopg2.connect(host="postgres", dbname="price", user="admin", password="admin")
# Create a cursor
cur = conn.cursor()

formatted_tuples = [('2021-12-03', 0, 53671.99), ('2021-12-04', 0, 49247.4233), ('2021-12-05', 0, 49454.1033), ('2021-12-06', 0, 50516.595), ('2021-12-07', 0, 50631.1267), ('2021-12-08', 0, 50510.235), ('2021-12-09', 0, 47591.0267), ('2021-12-10', 0, 47176.7617), ('2021-12-11', 0, 49388.085), ('2021-12-12', 0, 50105.7917), ('2021-12-13', 0, 46735.5167), ('2021-12-14', 0, 48385.125), ('2021-12-15', 0, 48886.06), ('2021-12-16', 0, 47645.4233), ('2021-12-17', 0, 46171.715), ('2021-12-18', 0, 46863.7717), ('2021-12-19', 0, 46695.385), ('2021-12-20', 0, 46913.6417)]

# Count rows in a table
cur.execute("SELECT COUNT(*) FROM currency")
row_count: int = cur.fetchone()[0]
if row_count == 0:
    cur.execute("INSERT INTO currency VALUES ( 0, 'USD', 'USD' )")

extras.execute_values(cur, "INSERT INTO price_data (time, currency_id, price) VALUES %s", formatted_tuples)

cur.execute("SELECT *  FROM price_data")
for row in cur:
    print(row)
