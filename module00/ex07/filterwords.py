import sys
import re

if len(sys.argv) != 3 or sys.argv[2].isdigit() is False\
   or sys.argv[1].isdigit() is True:
    print("ERROR")
    exit()
str = []
list = re.split(',|\'|!| |\.|\?|"|-|_|;|:', sys.argv[1])

for x in list:
    if len(x) > int(sys.argv[2]):
        str.append(x)
print(str)
