set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 445, 552}
print(set_numbers)

set_types = {1, 'hola', False, 12.11}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4,5,6,5,4]
set_numbers = set(numbers)
print(list (set_numbers))

size = len (set_countries)
print(size)
print('col' in set_countries)

# add

set_countries.add('pe')
print(set_countries)

# update

set_countries.update({'ar', 'ecua'})
print(set_countries)

# remove

set_countries.remove('col')
print(set_countries)

set_countries.clear()
print(set_countries)

set_countries_a = {'col', 'bol', 'mex'}
set_countries_b = {'bol', 'pe'}
print('union')
set_c = set_countries_a.union(set_countries_b)
print(set_c)
print(set_countries_a | set_countries_b)

print('intercepcion')

set_c = set_countries_a.intersection(set_countries_b)
print(set_c)
print(set_countries_a & set_countries_b)

print('Diferencia')
set_c = set_countries_a.difference(set_countries_b)
print(set_c)
print(set_countries_a - set_countries_b)

print('Diferencia simetrica')
set_c = set_countries_a.symmetric_difference(set_countries_b)
print(set_c)
print(set_countries_a  ^ set_countries_b)
