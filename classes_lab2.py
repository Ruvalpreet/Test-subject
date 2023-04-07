
import pandas as pd
from classes_lab import Building
class BuildingManager:

    def __init__(self):
        self.building = pd.DataFrame(columns=["name","location","floors","building_type"])

    def add_building(self,building):
        self.building.append({'name': building.get_name(), 'location': building.get_location(), 'floors': building.get_floors(), 'building_type': building.get_building_type()},ignore_index=True) 
    
    def remove_building(self,building):
        self.building = self.building[self.building["name"] != building.get_name()]
    
    def get_building_by_type(self,building_type):
        return self.building[self.building["building_type"] == building_type]
    
    def get_total_floors(self):
        return self.building["floors"].sum()
    
    def get_building_with_most_floors(self):
        return 0
    
    def __str__(self):
        return self.building