import time

def squaredecorator(function):

    def wrapper():
        x = function()
        return x**2

    return wrapper

@squaredecorator
def num_generator():
    return 10

def timeed(function):

    def wrapper(*args, **kwargs):
        before = time.time()
        value  = function(*args, **kwargs)
        after = time.time()
        spent = after - before
        fname = function.__name__
        print(f"function {fname} took {spent} seconds to run")
        return value

    return wrapper

@timeed
def myfunction(x):
    result = []
    for i in range(x):
        result.append(i)
    return result







# print(num_generator())

print(myfunction(100000))