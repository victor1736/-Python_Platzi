import sys
print(sys.path)

import re
text = 'Mi numero de telefono es 3107483273, el codigo del pais es 57, mi numero de a suerte es 7'

result = re.findall('[0-9]+',text)
print(result)

import time 
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,1,1,2,3,6,4,6,6,4,5,52,2,2,3]
counter = collections.Counter(numbers)
print(counter)