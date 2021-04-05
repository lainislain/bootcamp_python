import sys
import re

if len(sys.argv) != 3 or not sys.argv[2].isdigit()\
   or sys.argv[1].isdigit():
    print("ERROR")
    exit()
str = []
list = re.split(',|\'|!| |\.|\?|"|-|_|;|:', sys.argv[1])

for x in list:
    if len(x) > int(sys.argv[2]):
        str.append(x)
print(str)
