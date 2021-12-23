import random


def die_roll():
    roll = input("Would you like to roll a die? ")

    while roll == "yes" or roll == "y":
        print("Rolling the die...")
        print("The values are...")
        print(random.randint(1, 6))
        roll = input("Roll the die again? ")


die_roll()
