def highest_even(li):
    even = []
    for item in li:
        if item % 2 == 0:
            even.append(item)
    return max(even)
print(highest_even([1,10,2,3,4,8,11]))

#highest_even = [10, 2, 3, 4, 8, 11]
#highest_even.sort()
#while not max(highest_even) % 2 == 0:
#    if max(highest_even) % 2 == 1:
#        highest_even.pop()
#print(max(highest_even))