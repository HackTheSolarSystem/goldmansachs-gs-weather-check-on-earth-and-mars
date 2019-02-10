from ftplib import FTP
from PIL import Image
from io import BytesIO
import requests
import sys
import urllib.request

def main():
   args = sys.argv
   argLength = len(args)
   if argLength < 3:
       print ("Please provide FTP location, planet, date and time")
   else:
       ftpLocation = args[0]
       planet = args[1]
       date = args[2]
       if argLength == 4:
           time = args[3]
           print ("Hello ")#, ftpLocation, planet, date, time)
           #response = requests.get('https://pdsimage2.wr.usgs.gov/downloads/MARCI/data_B20/data_resx2/color/B20_day01_resx2.tiff')
           #print(response.status_code)
           #img = Image.open(BytesIO(response.content))
           #print(img)
           sink_path = 'C:/Users/archa/Desktop' 
           #resource = urllib.urlopen("http://www.digimouth.com/news/media/2011/09/google-logo.jpg")
           urllib.request.urlretrieve("https://pdsimage2.wr.usgs.gov/downloads/MARCI/data_B20/data_resx2/color/B20_day01_resx2.tiff", "local-img.tiff")
           print("done")
        #    output = open("file01.jpg","wb")
        #    output.write(response.content)
        #    output.close()



if __name__ == "__main__":
   main()
