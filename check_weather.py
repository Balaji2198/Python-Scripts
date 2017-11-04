#!/usr/share/env python3
#Python Program - Script to give a weather details for the user required city

import requests
#import os
from termcolor import colored
 
color = "yellow"
condition = True

while condition:
	#os.system('clear')
	print (colored("Developed by Balaji","green"))
	location = input("Enter the location: ")
	# your API ID goes here
	api_id = ''
	url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + api_id
	data = requests.get(url)
	read = data.json()
	temp = '%.2f' % float(read['main']['temp']-273)
	#temp_min = '%.2f' % float(read['main']['temp']-273)
	#temp_max = '%.2f' % float(read['main']['temp']-273)
	con = read['weather'][0]
	print (colored("Cityname: {} ".format(read['name']),color))
	print (colored("Temperature : {} °c".format(temp),color))
	print (colored("Country : {} ".format(read['sys']['country']),color))
	print (colored("Wind Speed : {} m/s".format(read['wind']['speed']),color))
	print (colored("Condition : {} ".format(con['main']),"yellow"))
	#print (colored("Minimum Temperature : {} ".format(temp_min),"yellow"))
	#print (colored("Maximum Temperature : {} ".format(temp_max),"yellow"))
	print (colored("Details : {} ".format(con['description']),"yellow"))
	ans = input("Do you want to check for other city(y/n)")
	if ans=='y':
		condition = True
	else:
		condition = False

print("Have a great Day")