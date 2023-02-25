my_dict = {}
print(type(my_dict))
my_dict = {
    'name':['Victor', 'alfonso'],
    'last_name':'Fernandez',
    'socond_last_name':'Hoyos'
}
print(my_dict)
print(len(my_dict))
print(my_dict['last_name'])
print(my_dict.get('age'))
my_dict['last_name'] = 'Alfonso'
print(my_dict)
my_dict['name'].append('kmkm')
print(my_dict)

del my_dict ['last_name']
print(my_dict)

print('items')
print(my_dict.items())

print('keys')
print(my_dict.keys())

print('values')
print(my_dict.values())


counter = 0
while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)