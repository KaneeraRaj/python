import random

lower_bound=1
upper_bound=10
max_attempt=12
secret_number=random.randint(lower_bound,upper_bound)

def get_guess():
    while True:
        guess=int(input("Guess a number between 1 to 10"))
        if lower_bound<=guess<=upper_bound:
          return guess
        else:
           print("Invalid input.Please enter the number between the specified range")

def check_guess(guess,secret_number):

           if guess==secret_number:
              return "Correct"
           elif guess <secret_number:
            return "too low"
           else:
               return "too high"
           
def play_game():
    attempts=0
    won=False

    while attempts <max_attempt:
     attempts+=1
     guess=get_guess()
     result=check_guess(guess,secret_number)
     if result=="Correct":
        print("Congratuations! You guessed the secret number{secret_number}in{attempts}attempts ")
        won=True
        break
     else:
        print(f"{result}Try again!")
    if not won:
        print("Sorry you ran out of attempts. the secret number is{secret_number}")

if __name__ =="__main__":
            print("Welcome to numbr guessing game")
            play_game()
               

              
        