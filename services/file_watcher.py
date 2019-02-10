import time  
import sys
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler 

#Global PATHS: 
PLANETS = {
            "PLANET_EARTH" : "EarthPath", 
            "PLANET_MARS"  : "MarsPath"
          }
PLANET = None

class eventHandler(PatternMatchingEventHandler):
    patterns = ["*.jpg"]
    def process(self, event): 
        print(event.src_path, event.event_type, "\n")

    def on_created(self, event):
        print("\n*** EVENT DETECTED: CREATE ***")
        print(PLANET)
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

if __name__ == '__main__':
    instantiatePlanet("PLANET_MARS").run() # Pass planet name here


