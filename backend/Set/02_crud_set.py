set_countries = {'Colombia','Mexico','bolivia'}
print(set_countries)

size = len(set_countries)
print(size)

print('Colombia' in set_countries)

# add

set_countries.add('Peru')
print(set_countries)

#update

set_countries.update({'Argentina', 'Ecuador', 'Peru'})
print(set_countries)

#Delete
set_countries.remove('Colombia')
print(set_countries)
set_countries.clear()
print(len(set_countries))