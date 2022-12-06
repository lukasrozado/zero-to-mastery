# Defining a function

#parameters
# Default Parameters = If no arguments are called use this default setup
def say_hello (name = "Clara", emoji = ";D"):
    print(f"Hello {name} {emoji}")
say_hello()
# Creating Variables to be called for arguments
def say_hello(name, emoji):
    print(f"Hello {name} {emoji}")

# Positional Arguments or invoke
# The values provided for a function
say_hello("Lukas", ":D")

# Keyword Argument (Bad Practice)
say_hello(emoji = ":D", name = "Bibi")

# Return
# I want to return everything because if i dont will return None

def sum (num1, num2):
    return num1 + num2
total = sum(4, 5)
print(sum(4, total))

# Functions modifies something or return something



