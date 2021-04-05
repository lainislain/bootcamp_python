import sys

def print_usage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("     python operations.py 10 3")

if (len(sys.argv) < 3):
    print_usage()
    exit()
elif (len(sys.argv) > 3):
    print("InputError: too many arguments\n")
    print_usage()
    exit()
elif not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("InputError: only numbers\n")
    print_usage()
    exit()
x = int(sys.argv[1])
y = int(sys.argv[2])
print(f"Sum:        {x + y}")
print(f"Diffrence:  {x - y}")
print(f"Product:    {x * y}")
if y == 0:
    print(f"Quotient:   ERROR (div by zero)")
    print(f"Remainder: ERROR (modulo by zero)")
else:
    print(f"Quotient:  {x / y}")
    print(f"Remainder: {x % y}")
