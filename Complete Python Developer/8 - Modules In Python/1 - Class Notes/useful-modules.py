from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

# li = [1, 2, 3, 4, 5, 6, 7, 7]
# sentence = "blah blah blah blah thinking about python"
# print(Counter(li))
# print(Counter(sentence))

dictonary = defaultdict(lambda: 5, {"a": 1, "b": 2})

print(dictonary["c"])


def function() -> object:
    return "does not exist"


dictonary = defaultdict(function, {"a": 1, "b": 2})

print(dictonary["c"])

d = OrderedDict()
d["a"] = 1
d["b"] = 2

d2 = OrderedDict()
d2["b"] = 2
d2["a"] = 1

print(d2 == d)

print(datetime.date.today())

# Arrays takes less memory then lists

arr = array("i", [1, 2, 3, 4, 5, 6, 7])
print(arr)