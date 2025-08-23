import random

def roll_dice():
    return random.randint(1,6)

def main():
    print("Welcome to the Dice Rolling Simulator")

    while True:
        user_input=input("Roll the dice(yes/no)").lower()

        if user_input=='yes':
            dice=roll_dice()
            print(f"\n You rolled a {dice}:")

        if dice==6:
            print("Great!You got the greatest number! ")

        if dice==1:
            print("Oops!You got the lowest number! ")

        else:
            print("Hmm!Nice roll!")

        if user_input=='no':
         print("Thanks for playing")
        break
    else:
     print("Please enter yes or no")
