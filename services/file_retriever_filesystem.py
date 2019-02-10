import sys
import os
from PIL import Image
from shutil import copyfile

def retrieve_from_server(planet_name, image_file_path, date_yyyyMMdd, time_hhmm):
    #add null checks for all input params
    planet_name = planet_name.upper()
    directory = get_directory(planet_name, date_yyyyMMdd)
    image_file_name=get_filename(image_file_path, date_yyyyMMdd, time_hhmm)
    image_file_extension = get_extension(image_file_path)

    copyfile(image_file_path, directory + image_file_name + image_file_extension)

    if image_file_extension != ".tiff":
        return convert_to_tiff(directory, image_file_name, image_file_extension)


def get_directory(planet_name, date_yyyyMMdd):
    slash = "/"
    directory = 'data' + slash + planet_name + slash + date_yyyyMMdd + slash
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def get_filename(file_name, date_yyyyMMdd, time_hhmm):
    if file_name.find('/') != -1:
        file_name_with_ext = file_name.rsplit('/', 1)[1]
    else:
        file_name_with_ext=file_name
    file_name = file_name_with_ext[0 : file_name_with_ext.index('.')]
    return file_name + "_" + date_yyyyMMdd + "_" + time_hhmm

def get_extension(file_path):
    if file_path.find('.') != -1:
        return "." + file_path.rsplit('.', 1)[1]
    else:
        return "."


def convert_to_tiff(directory, image_file_name, image_file_extension):
    img=Image.open(directory + image_file_name + image_file_extension)
    tiff_file_name = image_file_name+".tiff"
    img.save(directory + tiff_file_name)
    return tiff_file_name

if __name__ =='__main__':
    retrieve_from_server('mars', 'vine-1948358_1280_20180202_0000.png', '20180202', '0000')
