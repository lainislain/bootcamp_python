cookbook = {
    'sandwich': {'ingredients': 'ham, bread, cheese and tomatoes',
                 'meal': 'lunch', 'prep_time': '10 minutes'},
    'cake': {'ingredients': 'flour, sugar and eggs',
             'meal': 'dessert', 'prep_time': '60 minutes'},
    'salad': {'ingredients': 'avocado, arugula, tomatoes and spinach',
              'meal': 'lunch', 'prep_time': '15 minutes'},
}


def print_recipe(str):
    if str in cookbook:
        print(f"How to make {str}:")
        print(f"- Ingredients: {cookbook[str]['ingredients']}")
        print(f"- Meal: {cookbook[str]['meal']}")
        print(f"- Preparation Time: {cookbook[str]['prep_time']}\n")
    else:
        print("This recipe is not in the cookbook.\n")


def delete_recipe(str):
    if str in cookbook:
        cookbook.pop(str)
        print("Succefully deleted.\n")
    else:
        print("This recipe is not in the cookbook.\n")


def add_recipe(name_of_recipe, ingredients, meal, prep_time):
    cookbook[name_of_recipe] = {}
    cookbook[name_of_recipe]['ingredients'] = ingredients
    cookbook[name_of_recipe]['meal'] = meal
    cookbook[name_of_recipe]['prep_time'] = prep_time
    print("Succefully added.\n")


def print_all_recipe():
    print("All recipies:\n")
    for x in cookbook:
        print_recipe(x)


def print_message():
    print("Please select an option by typing to the corresponding number")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    print("6: Credits")
    return input("\n")


def print_credits():
    print("By amaghat | amaghat@student.1337.ma\n")


def choice(n):
    if n == "1":
        add_recipe(input("\nWrite the name of the recipe:\n"), input(
                         "The ingredients:\n"), input(
                        "What type of meal:\n"), input(
                         "Finally, the time of preparation:\n"))
        return True
    elif n == "2":
        delete_recipe(input("Write the name of the recipe you want delete:\n"))
        return True
    elif n == "3":
        print_recipe(input("Which recipe do you want to see:\n"))
        return True
    elif n == "4":
        print_all_recipe()
        return True
    elif n == "5":
        print("\nCookbook exited.")
        exit()
    elif n == "6":
        print_credits()
        return True
    else:
        return False


def recipe():
    n = print_message()
    while 1:
        if choice(n) is False:
            n = input("This option doesn't exist. Type 5 to quit.")
        else:
            n = print_message()


recipe()
