import os
import shutil
import sys

def transfer_data(planet_name, files_to_transfer, date_yyyyMMdd):
	
	allowed_planet_names = ['EARTH', 'MARS']
	slash = '/'
	underscore = '_'

	#TODO make sure we match this with what we have
	root = 'data'

	if planet_name not in allowed_planet_names: 
		raise Exception('Invalid planet name entered ' + planet_name)
	planet_name = planet_name.upper()
	vrt_folder = root + slash + planet_name + slash + date_yyyyMMdd 
	openspace_destination_folder = 'C:/Users/Pointy/Desktop/'+planet_name.lower()+'/'
	print('Preparing to move file... ')

	for file_name in files_to_transfer:
		shutil.copy(vrt_folder + slash + file_name, openspace_destination_folder)
		print('File copied from '+ vrt_folder + ' to '+ openspace_destination_folder)

if __name__ == "__main__":
   transfer_data('MARS',['comma-clipart-clipart-best-frrJZJ-clipart_20180202_0000.tiff'], '20180202')