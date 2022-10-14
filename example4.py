class PartyAnimal():
    """docstring for ."""
    x = 0
    name = ""

    def __init__(self, argument):
        self.name = argument
        print("Welcome to constructing a bot named:" ,argument)

    def party(self):
        self.x = self.x + 1
        print("value of constructor:",self.name,"is",self.x)

class FootballFan(PartyAnimal):
    """docstring for ."""
    points = 0

    def dance(self):
        self.points = self.points + 8
        self.party()
        print(self.name,"got points",self.points,"in dance")

male = PartyAnimal("Michael")
male.party()
print("\n","*********Next Call**************")
female = FootballFan("Jessica")
female.party()
female.dance()
