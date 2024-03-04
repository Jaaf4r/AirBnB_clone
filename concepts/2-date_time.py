import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current datetime:", current_datetime)

# Get the current date
current_date = datetime.date.today()
print("Current date:", current_date)

# Get the current time
current_time = datetime.datetime.now().time()
print("Current time:", current_time)

# Create a timedelta of 1 day
one_day = datetime.timedelta(days=1)

# Calculate tomorrow's date
tomorrow = current_date + one_day
print("Tomorrow's date:", tomorrow)
