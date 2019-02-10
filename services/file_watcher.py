import time  
import sys
import xmltodict
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler 
from shared_services import *


#Global PATHS: 
PLANETS = {
            "PLANET_EARTH" : "EarthPath", 
            "PLANET_MARS"  : "MarsPath"
          }
PLANET = None

class eventHandler(PatternMatchingEventHandler):
    #patterns = ["*.xml", "*.png"]
    def process(self, event): 
        print(event.src_path, event.event_type, "\n")

    def processEarth(self, event): 
        """
        EARTH FILE FORMAT NAME: 
        "ABI_TrueColor_YYYYMMDD_HHMMz.png"
        """
        print("Processing file for Earth")
        file_prefix = event.src_path.split(".")[0]
        arg1, arg2, date, time = file_prefix.split("_")
        file_name = event.src_path
        time = time[:4]
        print(file_name, date, time, "\n")
        # ---> insert code for processing Earth:
        return(file_name, date, time)

    def processMars(self, event): 
        """
        MARS FILE FORMAT NAME: 
        "B20_day01_resx2.xml" 
        """
        print("Processing file for Mars")
        extension = event.src_path.split(".")[1]
        if(extension == "xml"): 
            with open(event.src_path, 'r') as xml_source:
                xml = xml_source.read()
                parsed = xmltodict.parse(xml)
                file_name = parsed.get("Product_Observational", {}).get("Identification_Area", {}).get("title", {})
                stop_date_time = parsed.get("Product_Observational", {}).get("Observation_Area", {}).get("Time_Coordinates", {}).get("stop_date_time")
            date, time = stop_date_time.split("T")
            file_url = PLANETS[PLANET] + "/" + file_name
            date = "".join(date.split("-"))
            time = "".join(time.split(":")[:2])
            print(file_name, date, time, "\n")
            # --->insert code here for processing Mars:
            get_mars_daily_weather(file_name, date, time)
        else: 
            print("File" + event.src_path + "not in correct XML format. Ignoring.\n")

    def on_created(self, event):
        print("\n*** EVENT DETECTED: CREATE ***")
        if PLANET == "PLANET_EARTH": 
            self.processEarth(event)
        elif PLANET == "PLANET_MARS":
            self.processMars(event) 
        else: 
            self.process(event)

    def on_deleted(self, event):
        print("\n*** EVENT DETECTED: DELETE ***")
        self.process(event)

    def on_modified(self, event):
        print("*** EVENT DETECTED: MODIFIED ***")
        self.process(event)

class Observe(): 
    def __init__(self, source, planet):
        self.observer = Observer()
        self.PATH = source
        self.eventHandler = eventHandler()
        global PLANET
        PLANET = planet
        
    def run(self):
        self.start()
        try:
            while True:
                print("Heartbeat check: File monitoring in progress")
                time.sleep(5)
        except KeyboardInterrupt:
            self.stop()

    def start(self): 
        self.observer.schedule(self.eventHandler, self.PATH)
        self.observer.start()

    def stop(self): 
        self.observer.stop()
        self.observer.join()

#CALL FUNCTION: instantiatePlanet(PLANET_NAME).run()
class instantiatePlanet(): 
    def __init__(self, planet): 
        self.planet = planet
        self.PATH = None

    def setPath(self): 
        if self.planet in PLANETS: 
            self.PATH = PLANETS[self.planet]
        else: 
            print("Planet not supported. Please enter one of: ", PLANETS.keys())

    def run(self): 
        self.setPath()
        Observe(self.PATH, self.planet).run()

#if __name__ == '__main__':
#    instantiatePlanet("PLANET_EARTH").run() # Pass planet name here


