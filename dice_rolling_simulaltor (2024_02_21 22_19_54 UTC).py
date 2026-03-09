import random

def roll_dice():
    roll = input("Roll dice? (Yes/y) or (No/n): ")
    while roll.lower() == "yes" or roll.lower() == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))

        roll  = input("Roll again? (yes/y) or (no/n): ")


roll_dice()
