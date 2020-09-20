#!/bin/env python3

def timer(func):
    import time
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'func: {func.__name__} run {end-start} seconds')
    return inner

import time
from random import randint

@timer
def func1(a:int, b:int):
    time.sleep(randint(0,10))
    
@timer
def func2():
    time.sleep(randint(0,10))
    
@timer
def func3(i,host="xx"):
    time.sleep(randint(0,10))

func1(1,2)
func2()
func3(1,host='xy')