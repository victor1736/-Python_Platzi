number = []

for element in range(1,11):
    number.append(element)
print(number)


number2 = [element*2 for element in range(1,11) if element % 2 == 0]
print(number2)