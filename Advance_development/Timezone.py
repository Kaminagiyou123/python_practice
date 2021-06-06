from datetime import datetime,timezone,timedelta

print(datetime.now())
print(datetime.now(timezone.utc))
today=datetime.now(timezone.utc)
tomorrow=today+timedelta(days=1)

print(tomorrow)
print(today.strftime("%d-%m-%Y"))

user_date=input("Enter a date in YYYY-mm-dd: ")
user_date=datetime.strptime(user_date,"%Y-%m-%d")
print(user_date)