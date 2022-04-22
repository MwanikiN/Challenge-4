""" Python program to find the maximum and minimum values in a given list
of tuples using a lambda function """

def max_min_values(my_tuple):
    return_max = max(my_tuple,key=lambda item:item[1])[1]
    return_min = min(my_tuple,key=lambda item:item[1])[1]
    return return_max, return_min

print(max_min_values(my_tuple = [(2, 3), (4, 7), (8, 11), (3, 6)]))    