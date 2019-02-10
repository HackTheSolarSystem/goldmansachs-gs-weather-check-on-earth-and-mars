# goldmansachs-gs-weather-check-on-earth-and-mars
Partly Cloudy skies on the Earth and Mars

## GS@HackTheSolar: Real-Time Weather on Earth and Mars

### Goal
> To achieve Real-Time Data Visualization on OpenSpace 

### Approach
Enterprise Solution includes the following:
* Image Recorder - Watch for new weather images of the planet from Solar Systems and records the image, date and time 
* Image Processer - Imaging Library that processes any images to .tiff 
* Image Transformer - Georeferenced images transformed to global GDAL virtual dataset 
* OpenSpace GlobeBrowsing Visualization - GDAL dataset OpenSpace GlobeBrowsing Visualization
* OnDemand Visualization - Strategic solution for onDemand Visualization 

### Challenges
OpenSpace GlobeBrowsing Visualization with new geo.tiff/GDAL datasets
Image Transformer to GDAL VRT

### Tech Stack
* Python Flask Framework [FLASK]
* Python Imaging Library [PILLOW]
* Python URL Libraries [URLLIB]
* Watchdog Observers [WATCHDOG]
* Python shutil - high-level File Operations [SHUTIL]
* GDAL Virtual Dataset 
* OpenSpace

### Next Steps
* Using Hadoop - 1. stores large datasets reliably,
                 1. transforms datasets into georeference images and to global GDAL Virtual datasets
                 1. streams datasets at high bandwidth to OpenSpace GlobeBrowsing Visualization
                 

The Hadoop Distributed File System (HDFS) is designed to store very large data sets reliably, and to stream those data sets at high bandwidth to user applications. In a large cluster, thousands of servers both host directly attached storage and execute user application tasks.


### Contributers

@gs-engineers 
@thenu 
@indu 
@archana 
@zahra 
@shweta 
@emy 
@vandana 
@lakshmi
