#1
my_dict = {'Sonya': 2004, 'Liza': 2003, 'Lena': 1978}
print(my_dict)
print(my_dict['Sonya'])
print(my_dict.get('Ada'))
my_dict.update({'Anton': 1983, 'Tasya': 2009})
print(my_dict.pop('Sonya'))
print(my_dict)
#2
my_set = {1, 2, 3, True, 'String', 3, 2, True}
print(my_set)
my_set.update((7,8,9), (10,11,12))
my_set.discard(True)
print(my_set)