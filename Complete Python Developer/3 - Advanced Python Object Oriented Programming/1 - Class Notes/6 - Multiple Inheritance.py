#Parent Class
class User():

    def sign_in(self):
        print("logged in")

#Chidren Classes or SubClasses or Derived Classes
class Wizard(User):

    def __init__(self, name, power, email):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):

    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"Left-Arrows: {self.arrows}")

    def run(self):
        print("Ran really fast.")

# Multiple Inheritance
class HybridBord(Wizard, Archer):
    
    def __init__ (self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
archer1 = Archer("Robin", 100)
hybridbord1 = HybridBord("Borgie", 50, 100)

print(hybridbord1.arrows)

