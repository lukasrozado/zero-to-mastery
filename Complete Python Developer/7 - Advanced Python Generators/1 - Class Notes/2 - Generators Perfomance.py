from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"Took {t2 - t1} ms")
        return result
    return wrapper

@performance

def long_time():
    print("1")
    for i in range (10000000):
        i*5
@performance
def long_time2():
    print("1")
    for i in list(range(10000000)):
        i*5
long_time()
long_time2()