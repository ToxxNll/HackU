class human():
    def __init__(self,Iname,Ipol,Iage):
        self.name = Iname
        self.pol = Ipol
        self.age = Iage
        print ('This is construct')

    def work(self):
        if self.age<18:
            print("No")
        else:
            print("Yes")


class animal():
    def __init__(self,Atype,Ahabitation,Aage):
        self.type = Atype
        self.habitation = Ahabitation
        self.age = Aage

    def Change_type(self,new_type):
        print (f"You've changed your animals type from {self.type} to "+new_type)
        self.type = new_type

    def Change_habitation(self,new_habitation):
        print (f"You've changed your animals habitation from {self.habitation} to "+new_habitation)
        self.habitation = new_habitation

    def Change_age(self,new_age):
        print (f"You've changed your animals age from {self.age} to "+str(new_age))
        self.age = new_age
    
    def show_info(self):
        return self.type, self.habitation , self.age

class dog(animal):
    
    def Dvoice(self):
        print ("Bark")

    def olding(self):
        self.age += 1

Dog = dog("pet" , "mammal", 2)
Dog.Change_age(18)
Dog.Change_type("Shellfish")
Dog.Change_habitation("Water")
print (Dog.show_info())
# Tox = human("Tox" , "Male", 19)
# print(Tox.name)
# print(str(Tox.age) +' '+str(type(Tox.age)))




