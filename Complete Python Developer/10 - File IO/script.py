# my_file = open("test.txt")

# print(my_file.read()) Reads all the text
# print(my_file.readline()) Reads a line
# print(my_file.readlines())  # Reads and transform in a list

# my_file.close()
try:
    with open("test.txt", mode="a") as my_file:
        text = my_file.write("Hey it's me")
        print(text)
except FileNotFoundError as err:
    print("File Does not exist")
    raise err
