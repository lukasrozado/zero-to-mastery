# while condition:
#   something

i = 0
#infinite loop
while i < 50:
    print(i)
    i += 1
    break
else:
    print("Finish")
print("\n")
my_list = [1, 2, 3]

# FOR LOOP SAME AS WHILE
for item in my_list:
    print(item)
#SAME RESULT AS FOR
while i < len(my_list):
    print(my_list[i])
    i +=1
#BEST OPTION TO USE WHILE
while True:
    response = input("say something: ")
    if (response == "bye"):
        break
