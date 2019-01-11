#!/usr/bin/python

#bruno.on.the.road@gmail.com
#23/07/2016

#SERVICE REQUESTER

#The xmlrpclib module lets you communicate from Python with any XML-RPC server written in any language

import xmlrpclib

# XML multicall script (added by Ruben)
proxy = xmlrpclib.ServerProxy('http://localhost:9000')
multicall = xmlrpclib.MultiCall(proxy)
multicall.get_weather_station_location()
multicall.get_weather_station_coordinates()
multicall.get_date_time()
multicall.get_temperature()
multicall.get_wind_speed()
multicall.get_wind_direction()
result = multicall()
separator = "=" * 50
print("Weather Station: %s \nCoordinates: %s \nConditions recorded on: %s \n{}\n%s degrees Celcius \n%s Beaufort %s".format(separator) % tuple(result))


#proxy = xmlrpclib.ServerProxy('http://localhost:9000', verbose=True)
#print (proxy.system.listMethods())
#print "Weather station:", proxy.get_weather_station_location()
#print "Coordinates:", proxy.get_weather_station_coordinates()
#print ("=" * 50)
#print proxy.get_temperature(), "degrees Celcius"
#print proxy.get_wind_speed(), "Beaufort", proxy.get_wind_direction()
