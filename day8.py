'''🎯 Challenge
- Create a Car class with attributes and a display method'''

class Car: #class definiton
    def __init__(self, brand_name: str, colour: str,type: str): 
        self.brand_name=brand_name
        self.colour=colour
        self.type=type
    
    def show_details(self):
        print(f"Car details \n name:{self.brand_name} \n colour:{self.colour} \n type:{self.type} \n")    




# Object instantiation
tesla: Car = Car("Tesla","black","automatic")
tesla.show_details()

nano: Car = Car("Nano","white","gear")
nano.show_details()