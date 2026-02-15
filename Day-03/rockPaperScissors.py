
# identity operator (is) : a is a : true, a is b: false Checks if the memory location is same
# membership operator (in): a in list, a in dict, a in str, a in set  (checks if that a is a part of collection.)

import random, time


def checkWinner(player_choice:str, computer_choice:str):
        if(player_choice == computer_choice):
            print("It's a tie/draw.")
        elif(player_choice == "rock" and computer_choice == "scissors"):
            print("You won with rock! 🪨")
        elif(player_choice == "paper" and computer_choice == "rock"):
            print("You won with paper! 📃")
        elif(player_choice == "scissors" and computer_choice == "paper"):
            print("You won with scissors! ✂️")
        elif(player_choice == "scissors" and computer_choice == "rock"):
            print("The bot won with rock! 🪨")
        elif(player_choice == "paper" and computer_choice == "scissors"):
            print("The bot won with scissors! ✂️")
        elif(player_choice == "rock" and computer_choice=="paper"):
            print("The bot won with paper! 📃")

        # else:
        #     print("The bot wins")

# for the loading part
def threeDots(word: str, timer:float = 0.25, timesToloop:int = 3):
    """
    word => which word to be displayed besides the ... here.
    """
    count = 0
    while(count<timesToloop):
        print(f" {word} .    ", end="\r")
        time.sleep(timer)
        print(f" {word} ..  ", end="\r")
        time.sleep(timer)
        print(f" {word} ...", end="\r")
        time.sleep(timer)
        print("              ",end="\r" )
        count += 1
    
    


def confirmation(response:str)->bool:
    match response:
        case "y":
            return True
        case "n":
            return False
    return True

def main()->None:
    is_running = True
    while is_running:
        symbols : dict [str, str] = {
            "rock": "🪨",
            "paper": "📃",
            "scissors": "✂️"
        }
        threeDots("loading", 0.35, 2)
        print("\n\t-- Rock, Paper, Scissors --")

        player_choice: str = input("\nChoose rock ( 🪨  ), paper ( 📃 ), or scissors ( ✂️  ): ").strip().lower()
        computer_choice: str = random.choice(tuple(symbols))  
        #returns a random choice out of the symbols tuple (contains the keys of symbols)

        if(not(player_choice in symbols)):
            print("Invalid input detected.\nTry again.")
            continue
    
        print("\nResults:")
        print("--------------------------")
        print(f"You:      {symbols[player_choice]}  {player_choice}")
        print(f"Bot:      {symbols[computer_choice]}  {computer_choice}")
        print("")
        print("--------------------------")
        checkWinner(player_choice, computer_choice)
        print("--------------------------")

        response: str = input("\nContinue? (y/n) ").strip().lower()

        if(confirmation(response)):
            print("\033c", end="", flush=True)                  #clears the screen
            
            continue
        else:
            is_running = False

if __name__ == "__main__":
    main()







