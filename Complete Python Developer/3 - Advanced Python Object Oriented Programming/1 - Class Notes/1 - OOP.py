# We can divided ou code in classes so can be re-used and be organized in way for the future
# A way to think about our code and structure

# Class is a blueprint
# Moves to create a
# Intances creating a new object

# class BigObject: #Class
# code
#    pass
# obj1 = BigObject() #intanciate
# obj2 = BigObject() # Go in the memory and intanciate
#obj3 = BigObject()


class PlayerCharacter:
    #Class Object Atribute
    membership = True # This means that this is static doesnt change.


        #MAGIC METHOD
    def __init__(self, name= "anonymous", age = 0):
        #ATRIBUTES
        if PlayerCharacter.membership:
            if age > 18:    
                self.name = name #Self = Creates a Reference for something not created yet
                self.age = age # This is a atribute age.

    # METHODS IN A CLASS
    def shout(self):
        print(f"My name is {self.name}")
        return ("done")
    
    @classmethod
    def adding_things (cls, num1, num2):
        return num1 + num2
    @staticmethod
    def adding_things (num1, num2):
        return num1 + num2

player1 = PlayerCharacter("Illy", 21) #Intanciate Inicializes the Object. Calling the Class to start a object
#print(player1) # Stored in memory with diferrent locations not stored in the same location if created more
print(player1.name , player1.age)
print(player1.adding_things(2 ,3))
