class human():
    def __init__(self, iName, iPol, iAge):
        self.name = iName
        self.pol = iPol
        self.age = iAge
        print("This is construct")
    
    def olding(self):
        if type(self) != type(human):
            self.age -= 1
        else:
            self.age += 1
        
class baby(human):
    def __init__(self, iName, iPol, iAge,iToy,ICan_Walk):
        human.__init__(self,iName, iPol, iAge)
        self.toy = iToy
        self.can_walk = ICan_Walk
        print("This baby construct")
        
    def speak(self):
        if self.age >= 3:
            self.speaking = True
        else:
            self.speaking = False

    def olding(self):
        human.olding(self)

    def showinfo(self):
        try:
            return self.name, self.pol, self.age, self.toy, self.can_walk,self.speaking
        except:
            return self.name, self.pol, self.age, self.toy, self.can_walk
                

Dias = human("Dias", "Male", 23)
obj = baby("Tox", "Male", 9,'Buzzlighter',True)
obj.olding()
obj.speak()
print(obj.showinfo())
