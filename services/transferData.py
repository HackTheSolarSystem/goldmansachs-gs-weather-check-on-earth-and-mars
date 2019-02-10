import os
import shutil
import sys

def getPlanetWeatherData(planetName, date, time, destinationFolder):
	
	allowedPlanetNames = ['Earth', 'Mars']
	fileEnding = '.vrt'

	#to-do change this
	originFolder = '/Users/emyrivera/Desktop/clear_skies'

	if planetName not in allowedPlanetNames: 
		raise Exception('Invalid planet name entered ' + planetName)

	fileName = planetName + '_' + date + '_'+ time + fileEnding

	print('Preparing to move file... ')
	shutil.copyfile(originFolder + '/' +fileName, destinationFolder + '/' + fileName)
	print('file moved from '+ originFolder + ' to '+ destinationFolder)

if __name__ == "__main__":
   getPlanetWeatherData(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])