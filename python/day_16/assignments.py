# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()

print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted Date:", formatted_date)

# Calculate the time difference between 1 January 1970 and now.
epoch_start = datetime(1970, 1, 1)
now = datetime.now()
difference = now - epoch_start

years = difference.days // 365
months = (difference.days % 365) // 30
days = (difference.days % 365) % 30

print(f"Approx time: {years} years, {months} months, {days} days")
