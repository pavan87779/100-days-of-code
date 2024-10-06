import requests
#BBLA92J2ZWQDW1MRP2WAZUEH
#+15203948359
api_key = "0ea87ff05b78631fa786edc03bf2a7be"
TWILIO_ACCOUNT_SID = 'AC4a5ac1a0d2092f4b70b353a7e35913c0'
TWILIO_AUTH_TOKEN = '102fbf579e79dff8c3221a58de67faf7'
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="+15017122661",
    to="+15558675310",
)

print(message.body)

weather_params = {
    "lat": 28.704060,  # Latitude for your location
    "lon": 77.102493,  # Longitude for your location
    "appid": api_key,
    "cnt": 4  # Number of forecasts to retrieve
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()

data = response.json()
will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
