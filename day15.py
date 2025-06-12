# 🎯 Challenge
# - Create a decorator to log function execution time

import time
def timed(inner_func):
    def wrapper_func(*args,**kwargs):
        start=time.time()
        inner_func(*args,**kwargs)
        end=time.time()
        print("Time taken by the "+str(inner_func.__name__)+" is:  " +str((end-start)*1000)+" milliseconds" )
    return wrapper_func

@timed
def range_func(a):
    sum=0
    for i in range(a):
        sum+=a

print("\n\n\n\n\n")
range_func(10)
range_func(100)
range_func(1000000)