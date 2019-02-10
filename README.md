# goldmansachs-partly-clody-skies-on-the-earth-and-mars

# ZEPHYR : GS@HackTheSolar

### Goal
* To achieve Real-Time Data Visualization on OpenSpace 
* To provide OnDemand Data Visualization on OpenSpace

### Approach
Enterprise Solution includes the following:
* Image Recorder - Watch for new weather images of the planet from Solar Systems and records the image, date and time 
* Image Processer - Imaging Library that processes any images to .tiff 
* Image Transformer - Georeferenced images transformed to global GDAL virtual dataset 
* OpenSpace GlobeBrowsing Visualization - GDAL dataset OpenSpace GlobeBrowsing Visualization
* OnDemand Visualization - Strategic solution for onDemand Visualization 

### Challenges
* OpenSpace GlobeBrowsing Visualization with patched VRT datasets
* Image Transformation to VRT using GDAL

### Tech Stack
* Python Flask Framework [FLASK]
* Python Imaging Library [PILLOW]
* Python URL Libraries [URLLIB]
* Python GDAL Libraries [OSGEO]
* Watchdog Observers [WATCHDOG]
* Python shutil - high-level File Operations [SHUTIL]
* GDAL Virtual Dataset 
* OpenSpace

### Future Path
Set up a server to handle WMS requests and other requests to retrieve visualizations by planet/date and using Hadoop data clusters to
* store large datasets reliably either locally or on the cluster,
* transform datasets into georeference images and then to global GDAL Virtual datasets
* stream datasets at high bandwidth to OpenSpace GlobeBrowsing Visualization
      
### Lessons Learnt

      
### Contributors

* @gs-engineers 
* Thenu https://github.com/mthenu 
* Indu https://github.com/indumadu 
* Archana https://github.com/archanam90 
* Zahra https://github.com/zahramahmood 
* Shweta https://github.com/tyagishweta
* Emy https://github.com/emrivera  
* Vandana https://github.com/vandanah 
* Lakshmi Prasanna https://github.com/lethiraj
