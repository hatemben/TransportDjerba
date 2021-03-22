from datetime import datetime
import time
import json
import googlemaps

key = '' # Put google Maps API key here
traffic_model_key = 'best_guess'

client = googlemaps.Client(key)

origins = [{"lat": 33.872285, "lng": 10.858049}] # Houmet souk
destinations = [{"lat": 33.87927211, "lng": 10.87047879}] # Elwilaya

date = datetime.strptime('21 Mar 2017', '%d %b %Y')
departure = date.replace(hour=06, minute=30)

matrix = client.distance_matrix(origins, destinations,
                                    mode="driving",
                                    language="fr-FR",
                                    units="metric",
                                    departure_time=departure,
                                    traffic_model=traffic_model_key)

#duration best_guess in s
duration = matrix['rows'][0]['elements'][0]['duration']['value']

#distance in m
distance = matrix['rows'][0]['elements'][0]['distance']['value']

#duration in traffic s
duration_in_traffic = matrix['rows'][0]['elements'][0]['duration_in_traffic']['value']


#rows': [{u'elements': [{u'duration': {u'text': u'6 minutes', u'value': 349}, u'distance': {u'text': u'1,8 km', u'value': 1801}, u'duration_in_traffic': {u'text': u'6 minutes', u'value': 349}, u'status': u'OK'}]}], u'origin_addresses': [u'Houmt Souk, Tunisie'], u'destination_addresses': [u'Houmt Souk, Tunisie']}"
