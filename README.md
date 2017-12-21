This is a work in progress..

home_automation
Home automation with Python

Weather info is provided by https://www.wunderground.com data using their API. A low use API key is free. The weather data is pulled using a python3 script and spoken with festival. Edit the script with your API key and city and state data for weather. I run this script as a cron job in the mornings to tell us the weather as we are getting ready in the mornings.

I'd like to add a sprinkler function to disable my sprinklers when there is rain.

The lights are controlled by X10 modules and a bottlerocket controller. The bottle rocket is controlled by the bottlerock app found here: http://www.linuxha.com/bottlerocket/. Cron handles the timing. Some lights work well with their own script, while others are flipped on/off from cron directly. 

The update_times.py script checks the sunset times and updates the crontab entries to turn on lights 15 minutes before sunset. This script runs every few days.
