import requests
import time
from libs.openexchange import OpenExchangeClient

APP_ID="abc"

client=OpenExchangeClient(APP_ID)


usd_amount=1000
start_time=time.time()
gbp_amount=client.convert(usd_amount,'USD',"GBP")
end_time=time.time()

print(end_time-start_time)
print(f"USD {usd_amount} is GBP{gbp_amount:2f}")


usd_amount=1000
start_time=time.time()
gbp_amount=client.convert(usd_amount,'USD',"GBP")
end_time=time.time()

print(end_time-start_time)
print(f"USD {usd_amount} is GBP{gbp_amount:2f}")