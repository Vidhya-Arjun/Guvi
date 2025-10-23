from datetime import datetime, timedelta

# Get current date and time
current_datetime = datetime.now()

#segregate year, month and day from currentdate
segregated_datetime = lambda d: (d.year,d.month,d.day)
year,month,day = segregated_datetime(current_datetime)
print(f"The year is {year} \nThe month is {month} \nThe day is {day}")