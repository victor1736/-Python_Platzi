files= open('./text.txt')
print(files.read())

print(files.readline())
print(files.readline())
print(files.readline())
print(files.readline())

for line in files:
    print(line)
    
files.close()

with open('./text.txt') as files:
    for line in files:
        print(line)

#no abre en esta terminal solo en cmd
 