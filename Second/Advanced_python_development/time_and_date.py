from datetime import datetime
from datetime import timezone,timedelta

print(datetime.now())
print(datetime.now(timezone.utc))
tomorrow=datetime.now()+timedelta(days=1)
print(tomorrow)

print(tomorrow.strftime(('%m-%d-%Y')))