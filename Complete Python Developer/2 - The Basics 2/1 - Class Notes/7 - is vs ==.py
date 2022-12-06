# == Compare but not many restritctions doesnt have to be exactly

print(True == 1)
print('1' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# is Compare exacly the other one. Only in the same memory space.

print(True is 1)
print('1' is 1)
print([] is 1)
print(10 is 10.0)
#lists creates a new store of memory in different location. Will return false.
print([] is [])