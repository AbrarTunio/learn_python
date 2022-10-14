class PartyAnimal(object):
    """docstring for .x"""
    x = 0
    name = ''

    def __init__(self, nalo):
        self.name = nalo
        print("\n","Say hello to constructed",self.name)

    def party(self):
        self.x = self.x + 1
        print("\n",'executing party function for:', self.name)
        print("value stored in",self,"is",self.x)
        print(self.name,"Party Count",self.x)

element1 = PartyAnimal("Abrar")
element1.party()
element1.party()

print("\n","*******************************************")

element2 = PartyAnimal("Hussain")
element2.party()
element2.party()
