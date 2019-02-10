import gdal
import sys
import os

def createInfoFile(outputFileLocation, fileName):
    infoFile = open(outputFileLocation+fileName+".info",'w+')
    infoFile.write("Name="+fileName+"\n")
    infoFile.write("Identifier="+fileName+"\n")
    infoFile.write("ColorFile="+fileName+".vrt"+"\n")
    infoFile.write("HeightFile=nil")
    infoFile.close()
    
def generateVRTAndGeoTiff(inputFile,planet,date):
    titlePattern = "_geo"
    aullr = ""
    srs=""
    fileName,ext = os.path.splitext(inputFile)
    outputFileLocation = "/data/"+planet+"/"+date+"/"
    outputGeoFile = outputFileLocation+fileName+titlePattern+ext
    if(planet=="MARS"):
        aullr = '-180 90 180 -90'
        srs = 'EPSG:4326'
    ds = gdal.Open(inputFile)
    gdal.Translate(outputGeoFile, ds, format = 'GTiff', outputBounds = aullr, outputSRS = srs)
    gdal.BuildVRT(outputFileLocation+fileName+".vrt",outputGeoFile)
    createInfoFile(outputFileLocation, fileName)
