import sys
import os
import urllib.request
import requests
from PIL import Image


def retrieve_from_server(planet_name, image_file_path, meta_file_path, date_yyyyMMdd, time_hhmm):
    #add null checks for all input params
    planet_name = planet_name.upper()
    directory = get_directory(planet_name, date_yyyyMMdd)
    image_file_name=get_filename(image_file_path, date_yyyyMMdd, time_hhmm)
    meta_file_name=get_filename(meta_file_path, date_yyyyMMdd, time_hhmm)
    image_file_extension = get_extension(image_file_path)
    meta_file_extension = get_extension(meta_file_path)

    urllib.request.urlretrieve(image_file_path, directory + image_file_name + image_file_extension)
    urllib.request.urlretrieve(meta_file_path, directory + meta_file_name + meta_file_extension)

    if image_file_extension != ".tiff":
        convert_to_tiff(directory, image_file_name, image_file_extension)


def get_directory(planet_name, date_yyyyMMdd):
    slash = "/"
    directory = 'data' + slash + planet_name + slash + date_yyyyMMdd + slash
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def get_filename(file_name, date_yyyyMMdd, time_hhmm):
    if file_name.find('/'):
        file_name_with_ext = file_name.rsplit('/', 1)[1]
        file_name = file_name_with_ext[0 : file_name_with_ext.index('.')]
        return file_name + "_" + date_yyyyMMdd + "_" + time_hhmm

def get_extension(file_path):
    if file_path.find('.'):
        return "." + file_path.rsplit('.', 1)[1]


def convert_to_tiff(directory, image_file_name, image_file_extension):
    img=Image.open(directory + image_file_name + image_file_extension)
    img.save(directory + image_file_name + ".tiff")

if __name__ =='__main__':
    retrieve_from_server('mars', 'https://cdn.pixabay.com/photo/2017/01/03/02/07/vine-1948358_1280.png', 'https://minnlawyer.com/files/2017/04/comma-clipart-clipart-best-frrJZJ-clipart.jpg', '20180202', '0000')
