# Simplicity and Programming and use lists and dictionary to make a code clean and understandble
# Pure Functions = Something to happens to a function an return always the same thing

# Rules of Pure Functions
# 1 - Giving the same input will always be the same output.
# 2 - A functions should not produce sided effects.

# Pure Functions means less bug code.

def multiply_by2 (li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list
print(multiply_by2([5, 6, 10]))
