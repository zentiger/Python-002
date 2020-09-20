#!/bin/env python3

def sd_map(func,*args):
    it = []
    for i in range(len(args)):
        it.append(iter(args[i]))
    while True:
        li = []
        for i in range(len(it)):
            el = next(it[i])
            li.append(el)
        yield func(tuple(li))
