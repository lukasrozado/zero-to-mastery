#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1]) # [b] CORRECT
print(new_list[-2]) # [a] WRONG. DIDNT COUNT THE STOP...
print(new_list[1:3]) # ['b', 'c'] CORRECT
new_list[0] = 'z'
print(new_list) # ['z', 'b', 'c'] CORRECT

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list) # ['z', '2', '3'] CORRECT
print(bonus) # [1, 2, 3, 5] CORRECT