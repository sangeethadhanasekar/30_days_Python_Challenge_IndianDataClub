# 🎯 Challenge
# - Extend Car into an ElectricCar subclass with battery capacity

class Car: #class definiton
    def __init__(self, brand_name, colour,type): 
        self.brand_name=brand_name
        self.colour=colour
        self.type=type
    
    def show_details(self):
        print(f"\n Car details \n name:{self.brand_name} \n colour:{self.colour} \n type:{self.type} \n")    



class ElectricCar (Car):
    def __init__(self, brand_name, colour,type,battery_capacity): 
        super().__init__(brand_name,colour,type)
        self.battery_capacity= battery_capacity

    def show_batter(self):
        print("\n Battery settings is", self.battery_capacity)

ec=ElectricCar("Tesla","black","gear","100kwH")
ec.show_details()
ec.show_batter()