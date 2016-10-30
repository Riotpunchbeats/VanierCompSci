#Using higher order funtion reduce(), write a function max_in_list() that takes a list of numbers...

ips = [int(x) for x in input("Please enter a list of numbers you'd like evaluated: ").split()] #Actual split function. Iterates over input and returns a list

from functools import reduce #IMPORT HIGHER ORDER FUNCTION REDUCE

def max_in_list(numbers):
    return reduce(max, numbers) #Higher order function reduce() used for finding max. 


print (max_in_list(ips))
