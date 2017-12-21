from urllib.request import urlopen
import json
import subprocess

# API key and location data
api_key = 'EDIT_HERE_'
state = 'CA'
city = 'EDIT_HERE'

# Any string passed will pass to fesival for speech
def say(phrase):
    subprocess.call('echo '+phrase+'|/usr/bin/festival --tts',shell=True)

# Get Current Weather #
url = 'http://api.wunderground.com/api/'+api_key+'/conditions/q/'+ state + '/' + city + '.json'
response = urlopen(url).read().decode("utf-8")
parsed_json = json.loads(response)

temp = parsed_json['current_observation']['temp_f']
wind_mph = parsed_json['current_observation']['wind_mph']
wind_dir = parsed_json['current_observation']['wind_dir']
wind_str = parsed_json['current_observation']['wind_string']
rain_in = parsed_json['current_observation']['precip_today_in']
weather = parsed_json['current_observation']['weather']
visibility = parsed_json['current_observation']['visibility_mi']
feels_like = parsed_json['current_observation']['feelslike_f']


# Get Forecast Weather #
url = 'http://api.wunderground.com/api/'+api_key+'/forecast/q/'+ state + '/' + city + '.json'
response = urlopen(url).read().decode("utf-8")
parsed_json = json.loads(response)
# Now
now_forecast = parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext']
now_when = parsed_json['forecast']['txt_forecast']['forecastday'][0]['title']
# Next
next_forecast = parsed_json['forecast']['txt_forecast']['forecastday'][1]['fcttext']
next_when = parsed_json['forecast']['txt_forecast']['forecastday'][1]['title']
# Later
later_forecast = parsed_json['forecast']['txt_forecast']['forecastday'][2]['fcttext']
later_when = parsed_json['forecast']['txt_forecast']['forecastday'][2]['title']

# Get Astronomy Forecast
url = 'http://api.wunderground.com/api/'+api_key+'/astronomy/q/'+ state + '/' + city + '.json'
response = urlopen(url).read().decode("utf-8")
parsed_json = json.loads(response)
# Sunset Time
sunset_hr = int(parsed_json['sun_phase']['sunset']['hour'])%12
sunset_min = int(parsed_json['sun_phase']['sunset']['minute'])
# Sunrise Time
sunrise_hr = int(parsed_json['sun_phase']['sunrise']['hour'])
sunrise_min = int(parsed_json['sun_phase']['sunrise']['minute'])

forecast_msg = "The current weather for "+now_when+ " is "+now_forecast+". "+next_when+" the forecast is "+next_forecast+"."

sunrise_sunset_msg = "Sunrise today is at "+ str(sunrise_hr) + ":"+ str(sunrise_min) + ". Sunset tonight is at "+ str(sunset_hr) + ":"+ str(sunset_min)+". "

print(forecast_msg)
say(forecast_msg)

print(sunrise_sunset_msg)
say(sunrise_sunset_msg)  
