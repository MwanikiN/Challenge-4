""" Python program to sort a list of dictionaries using Lambda. """

def sort_dictionaries(data):
  sorted_dict = sorted(data, key = lambda i: i['gender'])
  return sorted_dict

data = [{'name':'Nimah', 'age':16, 'gender':'female'}, {'name':'Kelly', 'age':6, 'gender':'Male'}, {'name':'Ned', 'age': 7, 'gender':'Male'}]
print(sort_dictionaries(data))