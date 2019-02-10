import os
import shutil
import sys

def get_planet_weather_data(file_name, planet_name, date_yyyyMMdd):
	
	allowed_planet_names = ['Earth', 'Mars']
	slash = '/'
	underscore = '_'
	root = '/Users/emyrivera/Desktop'
	origin_folder = '/Users/emyrivera/Desktop/clear_skies'

	if planet_name not in allowed_planet_names: 
		raise Exception('Invalid planet name entered ' + planet_name)

	destination_folder = root + slash + planet_name + slash + date_yyyyMMdd 

	if not os.path.isdir(destination_folder):
		os.makedirs(destination_folder)

	print('Preparing to move file... ')
	shutil.copy(origin_folder + slash + file_name, destination_folder)
	print('File moved from '+ origin_folder + ' to '+ destination_folder)

if __name__ == "__main__":
   get_planet_weather_data(sys.argv[1], sys.argv[2], sys.argv[3])