numbers = [1,2,3,4,5,6]
numbers_v2 = []
for i  in numbers:
    numbers_v2.append(i*2)
    
print(numbers)
print(numbers_v2)

numbers_v3 = list(map(lambda i : i *2 ,numbers))
print(numbers_v3)

numbers_1 = [1,2,3,4,5]
numbers_2 = [7,8,9,2]

result =list (map(lambda x, y: x + y,numbers_1,numbers_2))
print(result)