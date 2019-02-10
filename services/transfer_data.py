import os
import shutil
import sys

def transfer_data(planet_name, vrt_file_name, date_yyyyMMdd):
	
	allowed_planet_names = ['Earth', 'Mars']
	slash = '/'
	underscore = '_'

	#TODO make sure we match this with what we have
	root = '../'
	origin_folder = '../whateverFolderNameItIs'

	if planet_name not in allowed_planet_names: 
		raise Exception('Invalid planet name entered ' + planet_name)

	destination_folder = root + slash + planet_name + slash + date_yyyyMMdd 

	if not os.path.isdir(destination_folder):
		os.makedirs(destination_folder)

	print('Preparing to move file... ')
	shutil.copy(origin_folder + slash + vrt_file_name, destination_folder)
	print('File moved from '+ origin_folder + ' to '+ destination_folder)

if __name__ == "__main__":
   transfer_data(sys.argv[1], sys.argv[2], sys.argv[3])