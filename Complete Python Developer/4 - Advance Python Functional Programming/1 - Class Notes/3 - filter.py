my_list = [1 ,3 ,5, 6, 10]

def only_odd(item):
    return item % 2 == 1

print(list(filter(only_odd, my_list))) # This way doesnt affect the outside just stay with pure functions
print(my_list)  