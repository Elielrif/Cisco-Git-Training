#!/usr/bin/env python3
"""module.py - an example of Python module"""

print(" I want to be a module")
print(__name__)

__counter = 0

def suml(list):
    global __counter
    __counter += 1
    sum = 0
    for e1 in list:
        sum += e1
    return sum

def prodl(list) :


    global __counter
    __counter += 1
    prod = 1
    for e1 in list:
        prod *= e1
    return prod


if __name__=="__main__":
    print("i pref to be module")
    l = [i+1 for i in range(5)]
    print(suml(l) == 15)
    print(prodl(l) == 120)