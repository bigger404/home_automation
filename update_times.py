#!/usr/bin/python3
from urllib.request import urlopen
import json
from crontab import CronTab
import datetime

#pip3 install --user python-crontab
#cron.remove_all(comment='foo')

#this currently only updates one device

# API key and location data
api_key = 'EDIT_HERE_'
state = 'CA'
city = 'hayward'

# Edit the name of the user account CronTab to use
username = 'EDIT_HERE'
my_cron=CronTab(user=username)

# X10 House number
house = 'b'

# Bottlerocket device name
br_dev = '/dev/ttyS0'

# Edit the lights out time in 24hr format
lights_out = 20

# Add lights to control and their X10 module number
lights = [1,5]

# Get Sunset time
url = 'http://api.wunderground.com/api/'+api_key+'/astronomy/q/'+ state + '/' + city + '.json'
response = urlopen(url).read().decode("utf-8")
parsed_json = json.loads(response)
# Sunset Time
sunset_hr = int(parsed_json['sun_phase']['sunset']['hour'])
sunset_min = int(parsed_json['sun_phase']['sunset']['minute'])

# On time is 15 minutes before sunset
on_hr = sunset_hr
on_min = (sunset_min-15)%60
if sunset_min <15:
    on_hr = sunset_hr -1

sched_on = str(on_min)+' '+str(on_hr)+' * * *'
cmd_on = 'br -x '+br_dev+' '+house+str(lights[0])+' ON'
cmd_off = 'br -x '+br_dev+' '+house+str(lights[0])+' OFF'

# Remove previous
my_cron.remove_all(comment='Device'+str(lights[0])+'ON')

# Add on entry
job = my_cron.new(command=cmd_on, comment='Device'+str(lights[0])+'ON')
job.setall(sched_on)

# Write the changes to CronTab
my_cron.write()

# handy debug function
def show_cron():
    for job in my_cron:
        print(job)
