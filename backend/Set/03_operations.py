set_a = {'Colombia', 'Mexico', 'Bolivia'}
set_b = {'Peru', 'Bolivia'}

#Union
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#Intercepción
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#diferencia
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#diferencia simetrica
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)