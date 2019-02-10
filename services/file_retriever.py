
import sys
import os
import urllib.request
import requests

def retrieveFromServer(planet_name, image_file_path, meta_file_path, date_yyyyMMdd, time_hhmm):
    #add null checks for all input params
    planet_name = planet_name.upper()
    print (image_file_path, meta_file_path, planet_name, date_yyyyMMdd, time_hhmm)
    #get image and meta data from url and store it in local file location
    urllib.request.urlretrieve(image_file_path, get_file_location(planet_name, image_file_path, date_yyyyMMdd, time_hhmm))
    urllib.request.urlretrieve(meta_file_path, get_file_location(planet_name, meta_file_path, date_yyyyMMdd, time_hhmm))
    #convert image to tiff

def get_file_location(planet_name, file_path, date_yyyyMMdd, time_hhmm):
    if file_path.find('/'):
        file_name_with_ext = file_path.rsplit('/', 1)[1]
        extension = file_name_with_ext.rsplit('.', 1)[1]
        file_name = file_name_with_ext[0 : file_name_with_ext.index('.')]
        return get_directory(planet_name, date_yyyyMMdd) + file_name + '_' + date_yyyyMMdd + '_' + time_hhmm + "." + extension

def get_directory(planet_name, date_yyyyMMdd):
    slash = "/"
    directory = 'data' + slash + planet_name + slash + date_yyyyMMdd + slash
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

if __name__ =='__main__':
    retrieveFromServer('mars', 'ftp://ftp.nnvl.noaa.gov/GOES/ABI_TrueColor/ABI_TrueColor_20180801_0000z.png', 'https://cdn.pixabay.com/photo/2017/01/03/02/07/vine-1948358_1280.png', '20180202', '0000')
