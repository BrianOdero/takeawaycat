# # class Bird:
# #     def __init__(self,name,color):
# #         self.name = name
# #         self.color = color
        
# #     def __str__(self):
# #         return "name " + self.name + "color " + self.color
    
# # class Fly(Bird):
# #     def __init__(self, name, color,maximum_altitude):
# #         super().__init__(name, color)
        
# #         self.maximum_altitude = maximum_altitude
        
# #     def __str__(self):
# #         return super().__str__() + "maximum altitude" + self.maximum_altitude
    
# # class Swim(Bird):
# #     def __init__(self, name, color,maximum_depth):
# #         super().__init__(name, color)
        
# #         self.maximum_depth = maximum_depth
        
# #     def __str__(self):
# #         return super().__str__() + "maximum_depth " + self.maximum_depth
    
    

# # flying_bird = Fly(name="hawk\n",color="black\n",maximum_altitude="200ft")
# # print(flying_bird)
    



# # #multilevel
# # class Bird:
# #     def __init__(self,name,color):
# #         self.name = name
# #         self.color = color
        
# #     def __str__(self):
# #         return "name " + self.name + "color " + self.color
    
    
# # class Fly(Bird):
# #     def __init__(self, name, color,maximum_altitude):
# #         super().__init__(name, color)
        
# #         self.maximum_altitude = maximum_altitude
        
# #     def __str__(self):
# #         return super().__str__() + "maximum altitude" + self.maximum_altitude
    
# # class Eat(Fly):
# #     def __init__(self, name, color, maximum_altitude,food):
# #         super().__init__(name, color, maximum_altitude)
        
# #         self.food = food
        
# #     def __str__(self):
# #         return super().__str__() + "Animal eats :" + self.food
    
    
# # #multiple 
# # class Eat(Fly,Swim):
    
# def add(a,b):
#     x = a + b
#     print(x)
    
# def add(a,b,c):
#     x = a + b + c
#     print(x)
    
# add(7,2)
# add(7,2,1)



class Employee:
    def message(self):
        print("This is employee class")
        
        
class Company(Employee):
    def message(self):
        print("This is company  class")
        
        
emp = Employee()
emp.message()



comp = Company()
comp.message()