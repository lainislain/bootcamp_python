from sys import argv
if len(argv) == 1:
    pass
elif len(argv) > 2 or argv[1].isdigit() == False:
    print("ERROR")
elif (int(argv[1])==0):
    print("I'm Zero")
elif (int(argv[1])%2==1):
    print("I'm Odd")
elif (int(argv[1])%2==0):
    print("I'm Even")

