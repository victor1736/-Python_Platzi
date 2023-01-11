dict = {}
for i  in range(1,5):
    dict[i] = i*2
print(dict)

dict_2 = { i: i*2 for i in range(1,5)}
print(dict_2)


import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
print(population)

population_v2 = {country : random.randint(1,100) for country in countries}
print(population_v2)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names,ages)))
    
new_dict = {name: ages for (name,ages) in zip(names,ages)}
print(new_dict)

import random
countries=['col', 'mex', 'bol', 'pe']
population_v3 = { country : random.randint(1,100) for country in countries }
print(population_v3)

result = { country: population for (country, population)in population_v3.items() if population>20}
print(result)

text = 'Hola, soy victor'
unique = {c : c.upper() for c in text if c in 'aeiou'}
print(unique)