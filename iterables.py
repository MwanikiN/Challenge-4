""" Python program to generate an infinite cycle of elements from an iterable """
import itertools as it

def infinite_cycle(iterable):
    loop = it.cycle(iterable)
    return loop

iter = infinite_cycle([1,2,3,4])
for element in iter:
  print (element)