from datetime import datetime, timedelta

today = datetime.now().date()
two_years_ago = today - timedelta(days=730)

print(today.isoformat())
print(two_years_ago.isoformat())