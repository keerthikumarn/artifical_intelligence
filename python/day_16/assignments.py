# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()

print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())
