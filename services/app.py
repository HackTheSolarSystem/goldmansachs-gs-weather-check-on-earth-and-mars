from flask import Flask
<<<<<<< HEAD
#from file_retriever import *
#rom config_parser import *
#from transfer_data import *
#from shared_services import *
from file_watcher import *

#import file_retriever
#import config_parser
#import transfer_data

import os

app = Flask(__name__)

@app.route('/')
@app.route('/welcome')
def HelloWorld():
    return "Welcome to Daily Weather!"


@app.route('/')
@app.route('/earth/daily-weather', methods=['GET'])
def get_earth_daily_weather_service():
    get_earth_daily_weather()


@app.route('/mars/daily-weather/<date_yyyyMMdd>', methods=['GET'])
def get_mars_daily_weather_service():
    instantiatePlanet("PLANET_MARS").run()

@app.route('/get/image/<planet_name>/<date_yyyyMMdd>/<time_hhmm>', methods=['GET'])
def get_image(planet_name, date_yyyyMMdd, time_hhmm):
    dir_name = '../data/' + planet_name + '/' + date_yyyyMMdd 
    allowed_planet_names = ['earth', 'mars']

    if planet_name not in allowed_planet_names: 
        raise Exception('Invalid planet name entered ' + planet_name)

    if not os.path.isdir(dir_name):
        return 'File not found.'

    file_names_dict = {}

    for f in os.listdir(dir_name):
        if not f.startswith('.'):
            split_file_name = f.split('.', 2)
            file_names_dict[int(split_file_name[0])] = f

    if time_hhmm in file_names_dict:
        return file_names_dict[time_hhmm]

    list_of_file_names = file_names_dict.keys()
    list_of_file_names.append(int(time_hhmm))
    list_of_file_names.sort()

    index_of_addition = list_of_file_names.index(int(time_hhmm))

    if index_of_addition == 0:
        return file_names_dict[list_of_file_names[1]]

    return file_names_dict[list_of_file_names[index_of_addition - 1]]

if __name__ == '__main__':
    get_mars_daily_weather_service()
   #app.run(debug=True)
   # get_file_location('MARS')
