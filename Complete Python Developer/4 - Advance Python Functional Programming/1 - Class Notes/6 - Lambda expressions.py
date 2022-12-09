from functools import reduce

my_list = [1 ,3 ,5, 6, 10]
your_list = [10 , 20, 30]

def multiply_by2 (item):
    return item * 2

print(list(map(lambda item: item*2, my_list))) # This way doesnt affect the outside just stay with pure functions
print(my_list)