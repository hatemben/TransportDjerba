#https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=33.872285,10.858049&destinations=33.87927211,10.87047879&mode=driving&language=fr-FR&key=******

# Houmet souk 33.872285,10.858049
# Elwilaya 33.87927211,10.87047879
Driving
{
   "destination_addresses" : [ "Houmt Souk, Tunisie" ],
   "origin_addresses" : [ "Houmt Souk, Tunisie" ],
   "rows" : [
      {
         "elements" : [
            {
               "distance" : {
                  "text" : "1,8 km",
                  "value" : 1801
               },
               "duration" : {
                  "text" : "6 minutes",
                  "value" : 349
               },
               "status" : "OK"
            }
         ]
      }
   ],
   "status" : "OK"
}
Transit :
{
   "destination_addresses" : [ "33.87927211,10.87047879" ],
   "origin_addresses" : [ "33.872285,10.858049" ],
   "rows" : [
      {
         "elements" : [
            {
               "status" : "ZERO_RESULTS"
            }
         ]
      }
   ],
   "status" : "OK"
}















