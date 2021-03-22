#import json

#matrix = "{u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'6 minutes', u'value': 349}, u'distance': {u'text': u'1,8 km', u'value': 1801}, u'duration_in_traffic': {u'text': u'6 minutes', u'value': 349}, u'status': u'OK'}]}], u'origin_addresses': [u'Houmt Souk, Tunisie'], u'destination_addresses': [u'Houmt Souk, Tunisie']}"

#print matrix['rows']
from datetime import datetime, timedelta
import time


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


departure_hour = 06
departure_min = 30
date = datetime.strptime('21 Mar 2017', '%d %b %Y')
departure = date.replace(hour=departure_hour, minute=departure_min)

departure = round_time(departure+timedelta(seconds=349))
print str(departure)[11:16]
## 349

