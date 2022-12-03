# String is a piece of a Text

#TYPE OF STRING
print("Strings \n")
print(type("Hello There"))

#LINE STRING

username = "SuperCoder"
password = "supersecret"

#LONG STRING

long_string = '''
I dont know what to do
so please
help me
'''

print(long_string)

# String Concatenation

print("String Concatenation\n")
first_name = "Lukas"
last_name = "Rozado"
full_name = first_name + " " + last_name
print(full_name)

print("Hello " + full_name)
print("\n")

#print("Hello" + 5) #TYPE ERROR BECAUSE ONLY WORK ONE NEEDS TO CONVERT

print("Types Conversion\n")
a = str(100)
b = int(a)
c = type(b)
print(type(a))
print(c)

# Escape Sequence

# \ Says to python to continue the string
weather = "It\'s \"kind of\" sunny"
tab = "\t"
new_line = "\n"
print(weather)

print(new_line)
# Formatted Strings

name = "Johnny"
age = 55
print("Formatted Strings")
print(new_line)
print("Hi " + name)
print(f"Hi {name} you have {age} years old")

print(new_line)

#String Indexes
print("String Indexes")

selfish = "me me me"
#          01234567
print(new_line)
print(selfish[0])
print(new_line)
print(selfish)

# [start: stop: stepover]

print(selfish[0:5])
print(selfish[0:8:2])
print(selfish[-3]) # THE NEGATIVE INVERT THE STRING
print(selfish[::-1]) # Invest al the string

#IMMUTABILITY

# Strings can't be change
# IT CAN BE ONLY REASSIGN

selfish = "01234567"
#selfish = "8"
selfish = selfish + "8"
print(selfish)