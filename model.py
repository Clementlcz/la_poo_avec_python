import json
import math

class Agent:

    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)

class Position:
    def __init__(self, longitude_degrees, latitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees

    @property
    def longitude(self):
        # Longitude in radians
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        # Latitude in radians
        return self.latitude_degrees * math.pi / 180

class Zone:
    
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    WIDTH_DEGREES = 1 # degrees of longitude

    def initialize_zones(self):
            for longitude in range(self.MIN_LONGITUDE_DEGREES, self.MAX_LONGITUDE_DEGREES, 

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = 0

def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(latitude, longitude)
        agent = Agent(position, **agent_attributes)
        print(agent.position.longitude)
        print(agent.position.latitude)

main()
