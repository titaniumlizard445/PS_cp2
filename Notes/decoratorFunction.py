#PS CP2 example of a decorator function

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Before doing math")
        func()
        print("After doing the math")
    return wrapper


@decorator
def greet():
    print("Hi")


greet()

@decorator2
def add():
    print(1+1)


add()

@decorator2
def subtract():
    print(10-4)

subtract()