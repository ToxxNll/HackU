class transport():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def getInfo(self):
        print(self.name, self.color , end=" ")
    
class car(transport):
    def __init__(self,name,color,kuzov,engine):
        self.kuzov = kuzov
        self.engine = engine
        super().__init__(name,color)

    def getInfo(self):
        super().getInfo()
        print (self.kuzov , self.engine)
    # def adding(self):
    #     self.kuzov = input("input type of Kuzov: ")
    #     self.engine = input("Input type of Engine: ")
        
class airplane(transport):
    def __init__(self,name,color,wings):
        self.wings = wings
        super().__init__(name,color)
    
    def getInfo(self):
        super().getInfo()
        print (self.wings)
    # def adding(self):
    #     self.wings = input("Input type of wings")

class bus(transport):
    def __init__(self, name, color, number, capacity):
        self.number = number
        self.capacity = capacity
        super().__init__(name, color)

    def getInfo(self):
        super().getInfo()
        print (self.number, self.capacity)
        
busObj = bus("Daewoo", "Red", 80, 1000)
busObj.getInfo()

planeObj = airplane("AirAstana","white",3)
planeObj.getInfo()

carObj = car("Subaru", "Blue","kuz","eng")
carObj.getInfo()
