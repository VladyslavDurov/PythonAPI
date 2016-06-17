from functools import wraps

#without params
def decor_a(fun_for_decor):
    @wraps(fun_for_decor)
    def wrapper(arg):
        print 'a: do something before'
        fun_for_decor(arg)
        print 'a: do something after'
    return wrapper

def decor_b(fun_for_decor):
    @wraps(fun_for_decor)
    def wrapper(arg):
        print 'b: do something before'
        fun_for_decor(arg)
        print 'b: do something after'
    return wrapper

@decor_b
@decor_a
def some_func_x(arg):
    print arg

@decor_a
@decor_b
def some_func_y(arg):
    print arg

some_func_x('What are you doing?')
print ''.join(20*'-')
some_func_y('What are you doing?')

