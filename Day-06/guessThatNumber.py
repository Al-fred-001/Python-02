
from typing import Final 
#Type Final is like a const declaration but only for developer : the program still runs just fine.

import random  
#for random number choice

#lower limit and upper limit inclusive
LOWER_LIMIT : Final[int] = 0
UPPER_LIMIT : Final[int] = 100
random_number : int = random.randint(LOWER_LIMIT, UPPER_LIMIT) 

# LOWER_LIMIT = 100  
#IDE shows red squiggly lines to denote cannot reassign to a type Final : though program runs.



#Helper function for printing bot message.
def bot_message(msg: str):
    print(f"Bot: {msg}")

def main()->None:
    print("")
    bot_message("Welcome to GuessThatNumber!")

    tries: int = 0;
    while True:
        try:
            user_guess:int = int(input("You: "))
        except ValueError as e:
            bot_message(f"{e}, Please use numbers only.")
            continue

        if(user_guess > random_number):
            bot_message("The number is lower.")
            tries +=1
        elif(user_guess < random_number):
            bot_message("The number is higher.")
            tries +=1
        else:
            tries +=1
            print("\n-------------------------------------------------------")
            bot_message(f"You guessed correct! You won in {tries} guesses.")
            print("-------------------------------------------------------\n")
            break


if __name__ == "__main__":
    main()

