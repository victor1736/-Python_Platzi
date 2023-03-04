import functools
numbers = [1,4,3,8]
result = functools.reduce(lambda counter,item:counter+item,numbers)
print(result)
