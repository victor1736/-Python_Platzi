sum = 0

for x in range(1,10):
    sum += x
print(sum)

def sum (a,b):
    sum=0
    for x in range(a,b):
        sum += x
    return sum

print (sum(1,100)) 

def find_volume(leng,width,depth):
    return leng*width*depth

print(find_volume(10,20,3))   