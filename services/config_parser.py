import configparser


def getConfigDetails(planetName):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[planetName]

def get_file_location(planet_name):
    planet_config = getConfigDetails(planet_name)
    return planet_config['FileLocation']

if __name__ =='__main__':
    get_file_location('MARS')
