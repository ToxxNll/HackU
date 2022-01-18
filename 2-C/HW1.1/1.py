class human():
    def __init__(self, iName, iPol, iAge):
        self.name = iName
        self.pol = iPol
        self.age = iAge
        print("This is construct")
    
    def olding(self):
        if type(self) == type(baby):
            self.age -= 1
        else:
            self.age += 1
        
class baby():
    def __init__(self, iName, iPol, iAge):
        self.name = iName
        self.pol = iPol
        self.age = iAge
        print("This is construct")
        
    def olding(self):
        human.olding(self)
        
Dias = human("Dias", "Male", 23)
obj = baby("qwe", "qwe", 9)
obj.olding()
print(obj.age)


# class human():
#     def __init__(self, iName, iPol, iAge):
#         self.name = iName
#         self.pol = iPol
#         self.age = iAge
#         print("This is construct")
    
#     def olding(self):
#         if type(self) == :
#             self.age -= 1
#         self.age += 1
        
# class baby(human):    
#     def olding(self):
#         human.olding(self)
        

# Dias = human("Dias", "Male", 23)
# obj = baby("qwe", "qwe", 9)
# obj.olding()
# print(type(obj))