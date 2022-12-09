from functools import reduce

my_list = [1 ,3 ,5, 6, 10]
your_list = [10 , 20, 30]
def only_odd(item):
    return item % 2 == 1

def acummulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(acummulator, my_list, 0)) # This way doesnt affect the outside just stay with pure functions
print(my_list)  