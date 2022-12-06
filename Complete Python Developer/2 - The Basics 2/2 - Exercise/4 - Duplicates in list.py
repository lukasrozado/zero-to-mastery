some_list =["a", "b" , "c", "b", "d", "m", "n", "n"]
duplicate = []
new_list = []

for letter in some_list:
    if letter not in new_list:
        new_list.append(letter)
    else:
        duplicate.append(letter)
print(duplicate)
