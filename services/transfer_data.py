import os
import shutil
import sys

def get_planet_weather_data(planet_name, date_yyyyMMdd, time_hhmm, destination_folder):
	
	allowed_planet_names = ['Earth', 'Mars']
	file_ending = '.vrt'
	slash = '/'
	underscore = '_'

	#to-do change this
	origin_folder = '/Users/emyrivera/Desktop/clear_skies'

	if planet_name not in allowed_planet_names: 
		raise Exception('Invalid planet name entered ' + planet_name)

	file_name = planet_name + underscore + date_yyyyMMdd + underscore + time_hhmm + file_ending

	print('Preparing to move file... ')
	shutil.copyfile(origin_folder + slash + file_name, destination_folder + slash + file_name)
	print('file moved from '+ origin_folder + ' to '+ destination_folder)

if __name__ == "__main__":
   get_planet_weather_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])