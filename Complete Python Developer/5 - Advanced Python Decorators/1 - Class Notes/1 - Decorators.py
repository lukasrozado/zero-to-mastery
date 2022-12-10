# Decorators supercharge the functions and add extra functionality

def hello():
    print("hellooooooooooooooo")
greet = hello # Because it's beeing called here python is smart and doesnt delete the function only the hello.
del hello
print(greet())

def hello(func):
    func()
def greet():
    print("Still Here")
a = hello(greet)

print(a)


#DECORATOR

def my_decorator(func):
    def wrap_func():
        print("******")
        func()
        print("******")
    return wrap_func

@my_decorator

def hello():
    print("helloooo")
hello()

@my_decorator
def bye():
    print("See ya later")
bye()
