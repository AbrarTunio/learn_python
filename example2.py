class PartyAnimal():
    """docstring for .PartyAnimal"""
    x = 1

    def __init__(self):
        print("I am constructed now")

    def party(self):
        self.x = self.x * 2
        print("Memory stores: ", self.x)

    def __del__(self):
        print("I am destructed oppsss")

var = PartyAnimal()
var.party()
var.party()

i = 0
count = 1
while i < 5:
    print(count,"=========>>number loop starting")
    var.party()
    i = i + 1
    print(count,"=========>>number loop ended")
    count = count +1


print("loop ends")

var = 42
print("Var contains new manual value that is: ", var)
