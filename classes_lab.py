
class Building:
    builder = "Ruval"
    def __init__(self, name, location , floors, building_type):
        self.__name =name
        self.__location = location
        self.floors = floors
        self.building_type = building_type
    
    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location
    
    def get_floors(self):
        return self.floors
    
    def get_building_type(self):
        return self.building_type
    
    def set_builder(cls,builder):
        cls.builder = builder
    
    def get_builder(cls):
        return cls.builder
        
    def __str__(self):
        return " quandile dingle"


