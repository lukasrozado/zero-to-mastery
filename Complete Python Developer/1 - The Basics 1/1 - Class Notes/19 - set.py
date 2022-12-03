# SET = UNORDER COLLECTION OF UNIQUE OBJECTS
# THERE IS NO DUPLICATE RESULTS IN THE SET
my_list = [1, 2, 3, 4 , 5, 5]
my_set = {1, 2 , 3 , 4, 5, 5}
my_set.add(100)
my_set.add(2)
print(my_set)
print(my_list[:-1])
print(set(my_list))

# There is no array points, sets is more like dictionary and you acess the value.

print(1 in my_set)

print(len(my_set))


# SET METHODS

your_set = {4,5,6,7,8,9}
#Shows the difference between my_set and your_set. All Duplicates between are ignored.
print(my_set.difference(your_set))
# Prints none because the 100 are discarded so it wont display nothing.
print(my_set.discard(100))
#printing the set here will show that the 100 was removed.
print(my_set)
#my_set.difference_update(your_set)
#print(my_set)

#Intersect
# Commom things between both
print(my_set.intersection(your_set))
print(my_set & your_set) # different way to do it

# Checking if there is something in commom

print(my_set.isdisjoint(your_set))

# UNION CONECT ALL THE SETS WITH NO DUPLICATES
print(my_set.union(your_set))
print(my_set | your_set) # Different way and more speed way to do it.

# It's inside of the other set ?
print(my_set.issubset(your_set))

# The inverse of subset
print(my_set.issuperset(your_set))
