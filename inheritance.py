class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname 
        self.age = age
        
        
        # def setFname(self,firstname):
        #     self.firstname=firstname
            
        # def getFname(self):
        #     return self.firstname
            
        # def setLname(self,lastname):
        #     self.lastname=lastname
            
        # def getLname(self):
        #     return self.lastname
            
        # def setAge(self,age):
        #     self.age=age
            
        # def getAge(self):
        #     return self.age
        
    def display(self):
        print("name :" {firstname} , {lastname} , {age})
        
        
class Student(Person):
    def __init__(self,firstname,lastname,age,regno,course):
        
        super().__init__(firstname,lastname,age)
        self.regno = regno
        self.course = course 
        
    def display(self):
        super().display()
        
       
        
        
# person = Person("John","wick",30)
# person.display()

student = Student(firstname="Tom",lastname="Hardy",age=20,regno="bcs",course="cs")
student.display()
        