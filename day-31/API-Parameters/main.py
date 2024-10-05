import requests
import datetime
from datetime import datetime

MY_LAT = 18.459261
MY_LONG = 79.136238

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,


}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)
