# def func (f) :
#     def wrap (*args, **kwargs) :
#         print ('start')
#         result = f(*args, **kwargs)
#         print ('end')
#         return result
#     return wrap

# @func
# def squared (x, y):
#     return x**2 + y**2

import time

def timer (f) :
    def wrapper (*args, **kwargs) :
        t1 = time.time()
        rv = f(*args, **kwargs)
        t2 = time.time()
        print ('Time :', t2-t1)
        return rv
    return wrapper

@timer
def test() :
    for _ in range (1000) :
        pass

@timer
def sleep_time (t) :
    time.sleep (t)
