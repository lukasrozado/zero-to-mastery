# It's a collection of itens list, dictionary , sets, lists, strings 
# iterate = > one by one check each item in the collection

users = {
    "name" : "Golem",
    "age" : 5006,
    "can_swim" : False
}

for item in users.items(): 
    print(item)
for item in users.values():
    print(item)
for item in users.keys():
    print(item)
for k,v in users.items():
    print(k, v)
# NOT ITERABLE 
#for item in 50
#   print(item)