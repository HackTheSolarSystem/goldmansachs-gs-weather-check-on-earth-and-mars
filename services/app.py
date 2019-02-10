from flask import Flask
#from file_retriever import *
#rom config_parser import *
#from transfer_data import *
#from shared_services import *
from file_watcher import *

#import file_retriever
#import config_parser
#import transfer_data

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

if __name__ == '__main__':
    get_mars_daily_weather_service()
   #app.run(debug=True)
   # get_file_location('MARS')
