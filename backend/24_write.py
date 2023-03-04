with open('./text.txt','r+') as files:
    for line in files:
        print(line)
    files.write('nuevas cosas en este archivo \n')