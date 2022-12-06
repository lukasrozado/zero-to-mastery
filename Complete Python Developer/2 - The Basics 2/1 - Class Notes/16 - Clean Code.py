def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
print(is_even(50))

# Clean Code
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(50))

# Cleaning Code
def is_even(num):
    if num % 2 == 0:
        return True
    return False
print(is_even(50))

# More Cleaner Code
def is_even(num):
    return num % 2 == 0
print(is_even(50))