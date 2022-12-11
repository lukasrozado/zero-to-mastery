# 1 - iterable
# 2 - Generator

#range (100)

#def make_list(num):
#    result = []
#    for i in range(num):
#        result.append(i*2)
#    return result
#my_list = make_list (100)
#print(my_list)

#Yield pauses the loop.

def generator_function(num):
    for i in range(num):
        yield i
for item in generator_function(100000):
    print(item)