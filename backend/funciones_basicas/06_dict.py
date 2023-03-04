import random
countries = ['Colombia', 'Mexico', 'Bolivia','Peru']

population_v2 = {country:random.randint(1,100) for country in countries}
print(population_v2)

result = { country : population for (country,population) in population_v2.items() if  population > 20 }
print(result)

text = 'Hola soy Victor'
unique = {c: c.upper() for  c in text if c in 'aeiou'}
print(unique)