li = [1,2,3,4,5]
li2 = ["a", "b", "c"]
li3 = [1, 2.5, "a", True]

#Data Structure
# Way to organize the information

amazon_cart = [
    "notebooks", 
    "toys",
    "grapes",
    "sunglasses"
]
print(amazon_cart[0:2])

# SLICING LISTS

#lists are mutable
amazon_cart[0] = "cars"
print(amazon_cart)
# Create a new copy of this list
new_cart = amazon_cart[:] #USED TO COPY THE ENTIRE STRING 
new_cart[0] = "gum"
print(new_cart)

# MATRIX - MULTI DIMENSIONAL LISTS

matrix = [
    [1,0,1],
    [0,1,0],
    [1,0,1]
]

print(matrix[0][1])

# LIST METHODS

basket = [1,2,3,4,5]
#ADDING
#new_basket = basket.append(100) doesnt work
basket.append(100) 
new_basket = basket
print(basket)
print(new_basket)
#insert
#POSITION AND THE VARIABLE
basket.insert(5, 5)
basket.extend([100])
new_basket = basket
print(new_basket)

#Removing

basket.pop()
basket.pop()
print(basket)
basket.remove(4)
print(basket)
basket.clear()
print(basket)

print("\n")

#Index

basket = ["a", "x", "p", "q", "e", "d"]
print(basket.index("d")) # LOOKS SOMETHING IN THE LIST
print("d" in basket)

# Count

print(basket.count("d"))

# Sort

#Modifies the list
basket.sort()
print(basket)
#creates a new copy of the list
print(sorted(basket))

# reverse same list
basket.reverse()
print(basket)

#CREATES A NEW LIST REVERSED
print(basket[::-1])

#NEW LIST WITH RANGE NUMBERS
print(list(range(1, 101)))

#sentence = " "
new_sentece = " ".join(["My", "Name" ,"Is"])
print(new_sentece)
print("\n")

# list unpacking

a,b,c, *other, d= [1 , 2, 3 , 4, 5, 6, 7]
print(a)
print(b)
print(c)
print(other)
print(d)

