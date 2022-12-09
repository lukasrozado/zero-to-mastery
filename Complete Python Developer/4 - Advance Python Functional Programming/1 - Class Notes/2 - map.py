my_list = [5, 6, 10]

def multiply_by2 (item):
    return item * 2

print(list(map(multiply_by2, my_list))) # This way doesnt affect the outside just stay with pure functions
print(my_list)