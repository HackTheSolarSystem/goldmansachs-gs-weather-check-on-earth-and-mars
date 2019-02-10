import time
import sys
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from services.app import get_mars_daily_weather
from services.app import get_earth_daily_weather

#Global PATHS: 
EARTH_PATH = "C:/Users/Pointy/Desktop/mars/test"  #Update Earth file path here
MARS_PATH = "C:/Users/Pointy/Desktop/mars/test"  #Update MARS file path here
PLANET_EARTH = "EARTH"
PLANET_MARS = "MARS"

class eventHandler(PatternMatchingEventHandler):
    patterns = ["*.jpg"]
    def process(self, event): 
        print(event.src_path, event.event_type, "\n")
        get_mars_daily_weather('20180202')


    def on_created(self, event):
        print("\n*** EVENT DETECTED: CREATE ***")
        self.process(event)

    def on_deleted(self, event):
        print("\n*** EVENT DETECTED: DELETE ***")
        #self.process(event)

    def on_modified(self, event):
        print("*** EVENT DETECTED: MODIFIED ***")
        #self.process(event)

class Observe(): 
    def __init__(self, source):
        self.observer = Observer()
        self.PATH = source
        self.eventHandler = eventHandler()
        

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
        self.MARS = MARS_PATH
        self.EARTH = EARTH_PATH
        self.PATH = None

    def setPath(self): 
        if self.planet == PLANET_EARTH:
            self.PATH = self.EARTH
        elif self.planet == PLANET_MARS: 
            self.PATH = self.MARS 
        else: 
            print("Not a valid planet: [Earth, Mars]")

    def run(self): 
        self.setPath()
        Observe(self.PATH).run()

if __name__ == '__main__':
    instantiatePlanet(PLANET_EARTH).run() # Pass planet name here


