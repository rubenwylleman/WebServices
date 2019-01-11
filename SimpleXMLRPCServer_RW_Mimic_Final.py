#!/usr/bin/python

#bruno.on.the.road@gmail.com
#23/07/2016

#SERVICE PROVIDER

#SimpleXMLRPCServer is the library to create an XML-RPC server


from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import logging
import random
import datetime


class RequestHandler(SimpleXMLRPCRequestHandler):
   rpc_paths = ('/RPC2',)

   def do_OPTIONS(self):
       self.send_response(200)
       self.end_headers()

   # Add these headers to all responses
   def end_headers(self):
       self.send_header("Access-Control-Allow-Headers", 
                        "Origin, X-Requested-With, Content-Type, Accept")
       self.send_header("Access-Control-Allow-Origin", "*")
       SimpleXMLRPCRequestHandler.end_headers(self)    

#Set up logging
logging.basicConfig(level=logging.DEBUG)

server = SimpleXMLRPCServer (('localhost', 9000),logRequests=True,requestHandler=RequestHandler)

#register XML-RPC introspextion functions such as system.listMethods()
server.register_introspection_functions()

#implement Multicall (added by Ruben)
server.register_multicall_functions()

#Expose functions

def get_weather_station_location():
	return "Oizy - Belgium"
server.register_function(get_weather_station_location)

def get_weather_station_coordinates():
	return "49.8966N-5.011E"
server.register_function(get_weather_station_coordinates)

def get_temperature():
	return random.randint(-20,40)
server.register_function(get_temperature)

def get_wind_direction():
	wind_directions = ['N','NE','E','SE','S','SW','W','NW']
	random.shuffle(wind_directions)
	return (wind_directions)[0]
server.register_function(get_wind_direction)

def get_wind_speed():
	return random.randint(0,12)
server.register_function(get_wind_speed)

def get_date_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
server.register_function(get_date_time)

try:
	print ('Use Control-C to EXIT')
	server.serve_forever()
except KeyboardInterrupt:
	print ('Exiting')	

class RequestHandler(SimpleXMLRPCRequestHandler):
   rpc_paths = ('/RPC2',)

   def do_OPTIONS(self):
       self.send_response(200)
       self.end_headers()

   # Add these headers to all responses
   def end_headers(self):
       self.send_header("Access-Control-Allow-Headers", 
                        "Origin, X-Requested-With, Content-Type, Accept")
       self.send_header("Access-Control-Allow-Origin", "*")
       SimpleXMLRPCRequestHandler.end_headers(self)    
