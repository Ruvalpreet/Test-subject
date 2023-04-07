from classes_lab import Building
from classes_lab2 import BuildingManager

first_building = Building("Ruval","canada",5,"stan grand")
sencond_building = Building("lavur","calgray",8,"stan gond")
third_building = Building("chad","vancover",9,"Walmart")

BuildingManager().add_building(first_building)
BuildingManager().add_building(sencond_building)
BuildingManager().add_building(third_building)

print(BuildingManager().get_building_by_type("Walmart"))
print(first_building,sencond_building,third_building)

print(BuildingManager().get_building_by_type("Walmart"))

