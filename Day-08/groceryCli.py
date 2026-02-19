from colorama import Fore, Back, Style, init
import os
import time

"""
To add/fix: 
    If user enters -200 or smth similar in price handle that case or adjust the usage.
    Colouring doesn't seem that nicely formatted. Fix that too.

"""

init(autoreset=True)

#defining variables for colouring: 

white = Fore.WHITE
black = Fore.BLACK
cyan = Fore.CYAN
yellow = Fore.YELLOW
blue = Fore.BLUE
red = Fore.RED
green = Fore.GREEN
magenta = Fore.MAGENTA
lightGreen= Fore.LIGHTGREEN_EX
bold = Style.BRIGHT
faint = Style.DIM
normal = Style.NORMAL
lightYellow = Fore.LIGHTYELLOW_EX
lightBlue = Fore.LIGHTBLUE_EX
lightCyan = Fore.LIGHTCYAN_EX

def threeDots(word: str, timer:float = 0.5, timesToloop:int = 3):
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
        count += 1

def Figlet():
    """
    Figlet generated online from normal text to figlet ansci art converter
    Like this: 
    font: ANSI Shadow
    """

    print(f"""{green}

 ██████╗ ██████╗  ██████╗  ██████╗███████╗██████╗ ███████╗██╗   ██╗     ██████╗██╗     ██╗
██╔════╝ ██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝    ██╔════╝██║     ██║
██║  ███╗██████╔╝██║   ██║██║     █████╗  ██████╔╝█████╗   ╚████╔╝     ██║     ██║     ██║
██║   ██║██╔══██╗██║   ██║██║     ██╔══╝  ██╔══██╗██╔══╝    ╚██╔╝      ██║     ██║     ██║
╚██████╔╝██║  ██║╚██████╔╝╚██████╗███████╗██║  ██║███████╗   ██║       ╚██████╗███████╗██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═════╝╚══════╝╚═╝
{white}
""")
# Combining styles



grocery_items : dict[str, dict[str, float]] = dict() # or {} 

#helper func for our program.
def Show_messsage(msg: str)->None:
    print(f"App: {msg}")

def Show_usuage()->bool:
    Show_messsage(f"""
<< -- {cyan}{bold}Usuage{normal} {white}-- >> 

    • {green}gl -add grocery-item-name <quantity> <price>
    • {green}gl -add --many {white}: For multiple inserts one after another.
        then use     : {green}grocery-item-name <price>{white}
        then         :  {green}'done' {white}or {green}enter blank to save.{white}

    • {green}gl -clear      {white}: clears the screen. (not the data but the screen)
    • {green}gl -help       {white}: displays the instructions when needed. 
    • {green}gl -exit       {white}: exit the app.
    • {green}gl -usuage     {white}: shows the usage for the app. 
    • {green}gl -list       {white}: displays the current items in the list.

    """)
    return True

def Show_instructions()->bool:
    Show_messsage(f"""
<< -- {cyan}{bold}Instructions{normal} {white}-- >> 
    1) Add the name of the grocery item with the price.
        Separate the item name and price with a space.
            • {green}gl -add grocery-item-name <price>{white}

    2) Use this format when the item name contains more than one word: 
            • {green}gl -add grocery-item-name <price>{white}
            eg: {magenta}gl -add black-jacket 200{white}

    3) If the item is in bulk (quantity of that same item > 1). Use this format: 
            • {green}gl- grocery-item-name <quantity> <price-per-item>{white}
            eg: {magenta}gl -add towels -3 100{white}

            {red}Note{white}: Here, 100 is the price for single towel.
            However, the net amount gets stored in the list.

    4) If multiple items are to be added. Use:
            • {green}gl -add --many
            grocery-item-1-name <quantity> <price>
            grocery-item-2-name <quantity> <price>{white}
            and so on. {blue}(quantity is optional){white}

    5) Some additional features: 
            • {green}gl -clear      {white}: clears the screen. (not the data but the screen)
            • {green}gl -help       {white}: displays the instructions when needed. 
            • {green}gl -exit       {white}: exit the app.
            • {green}gl -usuage     {white}: shows the usage for the app. 
            • {green}gl -list       {white}: displays the current items in the list.
    """)
    return True

# The main point for entry
def Start_app()->None:
    Figlet()
    threeDots("loading")
    print("\033c", end="", flush=True) 
    Show_instructions()
    commands: list[str] = ["-add", "-exit", "-clear", "-help", "-list"]
    while(True):
        user_input = input(f"{blue}Grocery-app-cli $ {lightCyan}").strip().lower().split(" ")
        if(is_invalid(cmd = user_input, commands=commands)):
            Show_usuage()
            continue
        if(not Exec_commands(user_input)):
            Show_usuage()
            continue


def Show_items():
    Show_messsage(f"\n-- {cyan}{bold}Printing grocery list.{normal}{white} --")
    i = 1
    for name, details in grocery_items.items():
        print(f"""
    -----------------------------------------
    ({i}) {lightCyan}{bold}{name.capitalize()}{normal}{white}
        {lightGreen}{bold}Quantity{normal}{white}     : {details["quantity"]}
        {lightGreen}{bold}Price{normal}{white}        : Rs.{details["price"]}/- per item
        {lightGreen}{bold}Total{normal}{white}        : Rs.{details["total"]}/-
        """)
        i += 1
    else:
        print("    -----------------------------------------\n\t-- End of List --") 
    return True  

# when gl -add -many is the command
def Add_multiple()->bool:
    Show_messsage(f"{lightYellow}Adding multiple items. Type 'done' to finish.{white}\nFormat: {green}grocery-item-1-name <quantity> <price>{white}")
    commands: list[str] = ["-add", "-exit", "-clear", "-help"]
    while True: 
        user_in = input(f"{lightBlue}Add item: {lightGreen}").strip().lower().split()
        
        
        if not user_in or user_in[0] == "done":
            break
        if user_in in commands and not user_in[0] == "gl":
            Show_usuage()
            continue

        try:
            name = user_in[0]
            if len(user_in) == 3 :
                # Handles -qty to qty input
                qty_str = user_in[1].replace("-", "") 
                qty = float(qty_str)
                price = float(user_in[2])
            elif len(user_in) == 2:
                qty = 1.0
                price = float(user_in[1])
            else:
                print(f"{red}Invalid format. Use: {green}name <qty> <price>{white}")
                continue

            
            grocery_items[name] = {
                "quantity": qty,
                "price": price,
                "total": qty * price
            }
            Show_messsage(f"{yellow}Added {name} (Total: {qty * price}){white}\n")

        except ValueError:
            Show_messsage(f"{red}Error: Please ensure quantity and price are numbers.{white}")
    return True


def Add_item(entered: list[str]):
    if len(entered) < 2:
        Show_messsage(f"{red}Missing arguments. Format: {green}gl -add <name> [qty] <price>{white}")
        return False

    name = entered[0]
    
    try:
        #for the following formats
        # Format: gl -add apple 1.50  (len=2)
        # Format: gl -add apple -3 1.50 (len=3)
        
        if len(entered) == 3:
            # remvove the "-" if it exists, then convert
            qty = float(entered[1].lstrip("-"))
            price = float(entered[2])
        else:
            qty = 1.0
            price = float(entered[1])

        grocery_items[name] = {
            "quantity": qty,
            "price": price,
            "total": qty * price
        }
        Show_messsage(f"{lightYellow}Successfully added {name} (Qty: {qty}, Total: {qty * price}){white}")
        return True

    except (ValueError, IndexError):
        Show_messsage(f"{red}Invalid input. Ensure price and quantity are numbers.{white}")
        return False

def Exec_commands(cmd):

    if cmd[1] == "-list": return Show_items()
    if cmd[1] == "-exit": 
        Show_messsage(f"{yellow}GoodBye ;)\n")
        os._exit(0)
    if cmd[1] == "-clear": 
        print("\033c", end="", flush=True) 
        return True
    if cmd[1] == "-help" : return Show_instructions() 
    if cmd[1] ==  "-usuage" : return Show_usuage()
    if len(cmd) < 3: 
        Show_messsage(f"{red}Missing essential arguments.{white}")
        return False
    if cmd[1] == "-add" and cmd[2] == "--many": return Add_multiple()
    if cmd[1] == "-add" : return Add_item(cmd[2:])
    # if not cmd[2].isalnum(): return False

def is_invalid(cmd, commands):
    if len(cmd) <=1 : return True
    if cmd[0] != "gl": return True
    if cmd[1] not in commands: return True
    return False



def main():
    Start_app()

if __name__ == "__main__":
    main()