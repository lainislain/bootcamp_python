from random import randint

lucky_number = randint(1, 99)

num = 0
n = 0
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")
while True:
    print("What's your guess between 1 and 99?")
    num = input(">> ")
    if num == "exit":
        print("Goodbye!")
        exit()
    else:
        if num.isdigit():
            num = int(num)
        else:
            print("That's not a number.")
            continue
    if num == lucky_number:
        if lucky_number == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if n == 0:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print(f"You won in {n+1} attempts")
        exit()

    elif num > lucky_number:
        print("Too high!")
    else:
        print("Too low!")
    n += 1
