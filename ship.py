class ship:
    def __init__(self,ship_name,ship_load,ship_location):
        self.ship_name = ship_name
        self.ship_load = ship_load
        self.ship_location = ship_location

    def get_shipName(self):
        return self.ship_name
    
    def set_shipName(self,name):
        self.ship_name = name
        
    def get_shipLoad(self):
        return self.ship_load
    
    def set_shipLoad(self,load):
        self.ship_load = load
        
    def get_shipLocation(self):
        return self.ship_location
    
    def set_shipName(self,location):
        self.ship_location = location
        
    def __str__(self):
        return "name" + {self.ship_name()} + "load" + {self.get_shipLoad() + "location" + {self.get_shipLocation()} }
        
    

ship = ship("Odero","Ziggo","Kakamega")

print(f"[SHIPNAME :] {ship.get_shipName()}")
