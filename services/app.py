from flask import Flask

app = Flask(__name__)
from file_retriever import *
from config_parser import *
from transfer_data import *


@app.route('/')
@app.route('/welcome')
def HelloWorld():
    return "Welcome to Daily Weather!"


@app.route('/')
@app.route('/earth/daily-weather', methods=['GET'])
def get_earth_daily_weather():
    # TODO FileWatcher - to watch for real time image from NASA/MARCI
    image_folder_name = getConfigDetails("EARTH")['FileLocation']
    retrieve_from_server('EARTH', 'https://minnlawyer.com/files/2017/04/comma-clipart-clipart-best-frrJZJ-clipart.jpg',
                         'https://cdn.pixabay.com/photo/2017/01/03/02/07/vine-1948358_1280.png', '20180202', '0000')
    return 'Successful'


@app.route('/mars/daily-weather/<date_yyyyMMdd>', methods=['GET'])
def get_mars_daily_weather(date_yyyyMMdd):
    # TODO FileWatcher - to watch for real time image from NASA/MARCI
    planet_name = 'MARS'
    # image_folder_name = get_file_location("MARS")
    # ge_folder_name = get
    # Step 2: Retrieve data from Space Systems
    tiff_file_name_with_ext = retrieve_from_server('MARS',
                                                   'https://minnlawyer.com/files/2017/04/comma-clipart-clipart-best-frrJZJ-clipart.jpg',
                                                   date_yyyyMMdd, '0000')
    # Step 3: Get georeferenced Tiff file, VRT file and Info file
    file_name = tiff_file_name_with_ext[0: tiff_file_name_with_ext.index('.')]
    list_of_interested_files = [file_name + '_geo.tiff', file_name + '.info', file_name + '.vrt']
    # Step 4: Transfer to local OpenSpace folder
    transfer_data(planet_name, list_of_interested_files, date_yyyyMMdd)
    print('Done!!')
    return 'Successful'


if __name__ == '__main__':
    get_mars_daily_weather('20180202')
   #app.run(debug=True)
   # get_file_location('MARS')
