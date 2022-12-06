# Scope - What variables do i have acess to ?
# Functions make part of a different location than variables
# Variables make part of a  global location
# Arguments and parameters are Local variables

#Why do we need scope ? And why this isn't all global 
# Because machines has limited resources limit power
# So we need to controll things unnecessary


# RULES

# 1 - Local Priority
# 2 - Parent Local?
# 3 - Global Priority
# 4 - built in function

a = 1 

def confusion():
    a = 5
    return a
print(a)
print(confusion())

a = 1 

def confusion():
    return a
print(a)
print(confusion())

def parent():
    a = 10
    def confusion():
        return a
    return confusion()
print(a)
print(parent())


# Global is a way to acess a function (But a bad practice)
total = 0 

def count():
    global total
    total += 1
    return total
count()
count()
print(count())

total = 0 

#Different way to do it but stay in local

def count(total):
    total += 1
    return total
print(count(count(count(total))))