class PartyAnimal():
    """docstring for ."""
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So Far",self.x)

an  = PartyAnimal()

an.party()
an.party()
an.party()
