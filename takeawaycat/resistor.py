

class Resistor:
    color = ["black","brown","red","orange","yellow",
 "green","blue","violet","grey","white"]

    def __init__(self):
        self.c1=None
        self.c2=None
        self.c3=None
        self.value=0.0
        
    def setC1(self,c1):
        self.c1=c1
        
    def setC2(self,c2):
        self.c2=c2
        
    def setC3(self,c3):
        self.c3=c3
    
    def setValue(self,value):
        self.value=value
        c1_index = Resistor.color.index(self.c1)
        c2_index = Resistor.color.index(self.c2)
        c3_index = Resistor.color.index(self.c3)
        self.value = (c1_index*10 + c2_index) * (10 ** c3_index)
        
    def getc1(self):
        return self.c1
    
    def getc2(self):
        return self.c2
    
    def getc3(self):
        return self.c3
    
    def getValue(self):
        return self.value
    
    
    def __str__(self):
        return " band1 :" + self.c1 + " band2 :" + self.c2 + " band3 :" + self.c3 + " value :" + str(resistor.getValue())
        
    
    
#calling the class

resistor = Resistor()
resistor.setC1("brown")
resistor.setC2("black")
resistor.setC3("orange")
resistor.setValue(0.0)

print(resistor.__str__())
