# For Loops.

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
special_for([1, 2, 3])

#Range
class MyGen():
    curret = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __iter__(self):
        return self
    def __next__ (self):
        if MyGen.curret < self.last:
            num = MyGen.curret
            MyGen.curret += 1
            return num
        raise StopIteration
gen = MyGen(0, 100)

for i in MyGen(0, 100):
    print(i)

    