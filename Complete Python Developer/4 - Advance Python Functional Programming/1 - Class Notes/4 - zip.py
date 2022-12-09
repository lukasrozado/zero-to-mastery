my_list = [1 ,3 ,5, 6, 10]
your_list = [10 , 20, 30]
def only_odd(item):
    return item % 2 == 1

print(list(zip(my_list, your_list))) # This way doesnt affect the outside just stay with pure functions
print(my_list)  