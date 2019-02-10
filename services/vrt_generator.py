import gdal
import sys
import os

def create_info_file(output_file_location, file_name):
    print("INFO:creating info file " + output_file_location+file_name+".info")
    info_file = open(output_file_location+file_name+".info",'w+')
    info_file.write("Name="+file_name+"\n")
    info_file.write("Identifier="+file_name+"\n")
    info_file.write("ColorFile="+file_name+".vrt"+"\n")
    info_file.write("HeightFile=nil")
    info_file.close()
    print("INFO:created info file")
    
def generate_vrt_and_geotiff(input_file,planet,date):
    title_pattern = "_geo"
    aullr = ""
    srs = ""
    file_name,ext = os.path.splitext(input_file)
    output_file_location = "/data/"+planet+"/"+date+"/"
    output_geo_file = output_file_location+file_name+title_pattern+ext
    print("INFO:getting geo spatial co-ordinates for planet " + planet)
    
    if(planet=="MARS"):
        aullr = '-180 90 180 -90'
        srs = 'EPSG:4326'
        print("INFO:MARS geo spatial co-ordinates found")
    if(planet=="EARTH"):
        aullr = 
        srs = 
        print("INFO:EARTH geo spatial co-ordinates found")
    if(planet=="MARS"||planet=="EARTH"):
        print("INFO:Loading input data set " + input_file)
        ds = gdal.Open(input_file)
        print("INFO:Translating input data set to geo tiff data set with output bounds " + aullr + " output srs " + srs)
        gdal.Translate(output_geo_file, ds, format = 'GTiff', outputBounds = aullr, outputSRS = srs)
        print("INFO:Building vrt for generated geo tiff data set")
        gdal.BuildVRT(output_file_location+file_name+".vrt",output_geo_file)
        create_info_file(output_file_location, file_name)
        print("INFO:Completed geo tiff, vrt and info files generation")
    else:
        print("DEBUG:Unknown planet")
