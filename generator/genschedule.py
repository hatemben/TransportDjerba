#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from datetime import datetime,timedelta
import time
import json
import googlemaps
import sys



## Config
## Done 10,14,18
ligne = 17
key = '' # Put google Maps API key here
traffic_model_key = 'best_guess'
currentDate = '22 Mar 2017'

extra_time_per_stop = 0 # stop time in seconds


## 

Last_station = 'Gachayin'
departure_hour = 18
departure_min = 15

reverse_way = 1

departure_hour_retour = 18
departure_min_retour = 40


## Util
def round_time(dt=None, date_delta=timedelta(minutes=1), to='average'):
    """
    Round a datetime object to a multiple of a timedelta
    dt : datetime.datetime object, default now.
    dateDelta : timedelta object, we round to a multiple of this, default 1 minute.
    from:  http://stackoverflow.com/questions/3463930/how-to-round-the-minute-of-a-datetime-object-python
    """
    round_to = date_delta.total_seconds()
    if dt is None:
        dt = datetime.now()
    seconds = (dt - dt.min).seconds
    if to == 'up':
        # // is a floor division, not a comment on following line (like in javascript):
        rounding = (seconds + round_to) // round_to * round_to
    elif to == 'down':
        rounding = seconds // round_to * round_to
    else:
        rounding = (seconds + round_to / 2) // round_to * round_to
	return dt + timedelta(0, rounding - seconds, -dt.microsecond)

## Init
client = googlemaps.Client(key)
date = datetime.strptime(currentDate, '%d %b %Y')
departure = date.replace(hour=departure_hour, minute=departure_min)


stops = []
with open('StationsBusDjerba.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	i = 0
	for row in spamreader:
		lat = row[0]
		lng = row[1]
		name = row[4]
		if (i > 0):
			#print "stop"+str(i)+" = schedule.AddStop(lng="+lat+", lat="+lng+", name=\""+name.strip()+"\")"
			stops.append({'i':i,'name':name.strip(), 'lat':row[1], 'lng': row[0]})
		i = i+1



destinations = ''
origins = ''
i = 0
with open('ligne'+str(ligne)+'.csv', 'rb') as csvfile:
	for row in list(csv.reader(csvfile)):
		row[0] = row[0].strip()
		if (i ==0):
			print "trip = route.AddTrip(schedule, headsign=\""+row[0]+" vers "+Last_station+"\")"
			first_element = row[0]
			i = i+1
		for item in stops:
			if item['name'] == row[0]:
				if (origins == '' and destinations ==''):
					origins = [{"lat": item['lat'], "lng": item['lng']}]
					display_time = str(departure_hour)+":"+str(departure_min)
					duration = 0
				else:
					if (destinations == ''):
						destinations = [{"lat": item['lat'], "lng": item['lng']}]
						matrix = client.distance_matrix(origins, destinations,
                                    mode="driving",
                                    language="fr-FR",
                                    units="metric",
                                    departure_time=departure,
                                    traffic_model=traffic_model_key)
						duration = matrix['rows'][0]['elements'][0]['duration']['value']
						origins = destinations
						destinations = ''
						departure = round_time(departure+timedelta(seconds=duration+extra_time_per_stop))
						display_time = str(departure)[11:16]
				pass
				print "trip.AddStopTime(stop"+str(item['i'])+", stop_time='"+display_time+":00') # "+item['name']+" - "+ str(duration)


if (not reverse_way):
	sys.exit()

print ''

date = datetime.strptime(currentDate, '%d %b %Y')
departure = date.replace(hour=departure_hour_retour, minute=departure_min_retour)
destinations = ''
origins = ''
i = 0
with open('ligne'+str(ligne)+'.csv', 'rb') as csvfile:
	for row in reversed(list(csv.reader(csvfile))):
		row[0] = row[0].strip()
		if (i == 0):
			print "trip = route.AddTrip(schedule, headsign=\""+row[0]+" vers "+first_element+"\")"
			i = i+1
		for item in stops:
			if item['name'] == row[0]:
				if (origins == '' and destinations ==''):
					origins = [{"lat": item['lat'], "lng": item['lng']}]
					display_time = str(departure_hour_retour)+":"+str(departure_min_retour)
					duration = 0
				else:
					if (destinations == ''):
						destinations = [{"lat": item['lat'], "lng": item['lng']}]
						matrix = client.distance_matrix(origins, destinations,
                                    mode="driving",
                                    language="fr-FR",
                                    units="metric",
                                    departure_time=departure,
                                    traffic_model=traffic_model_key)
						duration = matrix['rows'][0]['elements'][0]['duration']['value']
						origins = destinations
						destinations = ''
						departure = round_time(departure+timedelta(seconds=duration+extra_time_per_stop))
						display_time = str(departure)[11:16]
				pass
				print "trip.AddStopTime(stop"+str(item['i'])+", stop_time='"+display_time+":00') # "+item['name']+" - "+ str(duration)


