name = "Victor Alfonso"
last_name = "Fernandez Hoyos"
age = "30"
print(name)
print(last_name)

full_name = name + ' ' + last_name
print(full_name)

quote = "I'm Victor "
print(quote)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name + " y mi edad es "+ age
print('v1' ,template)

template = "Hola, mi nombre es {} y mi apellido es {} y mi edad es {}".format(name,last_name, age)
print('v2' ,template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y mi edad es {age}"
print('v3' ,template)