# Dictionary
dictionary = {
    "a" : [1, 2, 3],
    "b" : 2,
    "c" : "Hello"
}
my_list = {
    "a" : [1, 2, 3],
    "b" : 2,
    "c" : "Hello"
},
{
    "a" : [4, 5, 6],
    "b" : 2,
    "c" : "Hello"
}
print(my_list[0]["b"])
print(dictionary)

# A key from a Dictionarie needs to be imutable
# lists are mutable.
#my_dict = {
#    [100] : True
#}


# Way to avoid errors
user = {
    "name" : [1,2,3],
    "hello" : "Ok",
    "age" : 20
}
# print(user["age"]) #not the good way
# IF AGE DOESNT EXISTS USE 1
print(user.get("age", 1))

# Not the commom way
user2 = dict(name = "JohnJohn")
print(user2)

print("age" in user)
print("age" in user.values())
print(user.items())
user3 = user.copy()
print(user.clear())
print(user)
print(user3)
print(user3)
print(user3.update({"age" : 55}))
