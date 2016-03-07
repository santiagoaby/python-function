#!usr/bin/env python

def FuncOut(name,age):
    print "Hi! My name is", name + "and my age is" ,age
    print "Hi! My name is %s and my age is %d" %(name, age)
    print "Hi! My name is {} and my age is {}" .format(name,age)

FuncOut("Mary",19)
