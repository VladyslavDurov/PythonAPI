from functools import wraps

def decor(func):
    @wraps(func)
    def wrapper(*args):
        func()
        print(20*'+')
    return wrapper

#variant_1
@decor
def createGenerator1():
    mygenerator = (x**2 for x in range(3,5))
    for item in mygenerator:
        print(item)

#variant_2
@decor
def createGenerator2():
    def generator():
        for item in range(2,5):
            yield item**3
    for x in generator():
        print(x)

#variant_3
def createGenerator3():
    a = [1,2,3,5]
    my_generator = iter(a)
    for item in my_generator:
        print(item)

createGenerator1()
createGenerator2()
createGenerator3()



