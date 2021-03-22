import csv
import sys

reverse_way = 1
ligne = 18


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
			stops.append({'i':i,'name':name.strip()})
		i = i+1


if (not reverse_way):
	sys.exit()


i = 0
with open('ligne'+str(ligne)+'.csv', 'rb') as csvfile:
	for row in (list(csv.reader(csvfile))):
		row[0] = row[0].strip()
		if (i ==0):
			print "trip = route.AddTrip(schedule, headsign=\""+row[0]+" vers ...\")"
			first_element = row[0]
			i = i+1
		for item in stops:
			if item['name'] == row[0]:
				print "trip.AddStopTime(stop"+str(item['i'])+", stop_time='') # "+item['name']
				pass