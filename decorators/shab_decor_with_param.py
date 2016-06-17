from functools import wraps

#with params
def my_decor(param):
    def decor(fun_for_decor):
        @wraps(fun_for_decor)
        def wrapper(arg):
            print 'do something before'
            fun_for_decor(' '.join((arg, param,'?')))
            print 'do something after'
        return wrapper
    return decor

@my_decor('Kenny')
def some_func(arg):
    print arg

some_func('How killed')

