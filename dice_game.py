import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def game():
    firstPlayer = input("Enter player 1's name: ")
    secondPlayer = input("Enter player 2's name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(firstPlayer, "rolled", roll1)
    print(secondPlayer, "rolled", roll2)

    if roll1 > roll2:
        print(firstPlayer, "wins!")
    elif roll2 > roll1:
        print(secondPlayer, "wins!")
    else:
        print("Tie!")


game()        