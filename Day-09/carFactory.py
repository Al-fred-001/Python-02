from collections import Counter
from time import sleep
from colorama import Fore, Style
import random
import os


"""
To do: 
    Fix the various bugs (most likely present in the code)
    Reduce redundancy of the code. (Refactor code)
    Provide better keyword than the lengthy worker each time
    Provide color coding to a lot of things. (not proper output consistency.)
    Make the cli a bit more easier to use.
    Add a figlet of its own like that in Grocery Cli.
"""
# helper variables
theme = {
    # Standard Colors
    "w": Fore.WHITE,
    "black": Fore.BLACK,
    "c": Fore.CYAN,
    "y": Fore.YELLOW,
    "blue": Fore.BLUE,
    "r": Fore.RED,
    "g": Fore.GREEN,
    "m": Fore.MAGENTA,
    
    # Light/Ex Colors
    "lg": Fore.LIGHTGREEN_EX,
    "ly": Fore.LIGHTYELLOW_EX,
    "lb": Fore.LIGHTBLUE_EX,
    "lc": Fore.LIGHTCYAN_EX,
}

style = {
    # Text Styles
    0: Style.NORMAL,
    1: Style.DIM,
    2: Style.BRIGHT,
}

#helper function()
# first letter of each color and style repr the output color and style format.
def displayer(to_print:str, color:str= 'w', styled:int=0):
    start = theme[color]
    end = theme["w"]
    textStyle = style[styled]
    end
    print(f"{theme["y"]}{style[2]}Worker:{style[0]}{end} ", end="")
    print(f"{start}{textStyle}{to_print}{style[0]}{end}")


class Car:
    carsList :dict[str, 'Car'] = {}
    def __init__(self, brand:str, color:str, model:int, speedLimit:int):
        self.brand = brand
        self.color = color 
        self.model = model 
        self.speedLimit = speedLimit
        self.stock = 1
        self.sold = 0
        Car.carsList[self.brand] = self
        displayer(f"Successfully built {self.brand.capitalize()} [{self.color.capitalize()}]!", "g")
    def testRun(self):
        is_done = False
        while not is_done:
            try:
                speed = int(input("Test Speed (km/hr): "))

                if speed <= 0:
                    displayer(f"Speed must be greater than 0.", "ly")
                    continue

                distance = int((input("Distance to cover (km): ")))
            except ValueError as e:
                displayer("Please enter numerical values only","r")
                continue
            for i in range(int(distance)):
                sleep(60/speed)
                print(f"Travelled: {i+1} Km")
            else:
                displayer(f"\nTest-run Completed: {self.brand} is in good condition.", "lg")
                is_done = True

    def displayInfo(self)->None:
        print("-"*40)
        print(f"""
    -- Displaying info : {self.brand.capitalize()} --

        1) Brand          : {(self.brand).capitalize()}
        2) Color          : {self.color}
        3) Model          : {self.model}
        4) Speed limit    : {self.speedLimit}
        5) Owned          : {self.stock}
        6) Sold           : {self.sold}
    """)
        print("-"*40)

    def upgradeCar(self) -> None:
        prompt = input("Feature to modify: ").strip().lower()
        
        if prompt == "brand": 
            print("")
            print("Cannot change the brand of car.\nFor that purpose:")
            print("Option-01: Buy a new car\nOption-02: Exchange your current car.")
            print("")
            return

        attribute_to_change = prompt
        if prompt == "speed limit":
            attribute_to_change = "speedLimit"

        if hasattr(self, attribute_to_change):
            new_value = input(f"Enter the upgraded {prompt}: ")
            
            if(attribute_to_change == "speedLimit"):
                try:
                    final_value:str|int = int(new_value)
                except ValueError as e:
                    displayer(f"Error: {e}", "r")
                    return
            else:
                final_value = new_value
            setattr(self, attribute_to_change, final_value) 
            
            print(f"Successfully upgraded {prompt} to {new_value}!")
        else:
            print(f"Error: {prompt} is not a valid feature.")

    def buildCars(self, quantity:int):
        self.stock += quantity
        print(f"Successfully built {quantity} {self.brand} cars.")

    def sellCars(self, quantity:int):
        if(self.stock<quantity):
            print("Not enough cars available to sell.")
        else:
            self.stock -= quantity
            self.sold += quantity
            print("-"*30)
            displayer(f"{quantity} {self.brand.capitalize()}, sold successfully!", "ly")
            displayer(f"Details:\nStock      :{self.stock}\nSold       :{self.sold} ","lb")
            print("-"*30)


def display_usuage():
    # Header using displayer
    displayer("--- HOW TO OPERATE THE FACTORY ---", "c", 2)
    
    # Body using theme 
    usage_text = f"""
    • {theme['g']}worker -build <brand> <model> <speed_limit> <color>
    • {theme['g']}worker -add <brand> <quantity>
    • {theme['g']}worker -test <brand>
    • {theme['g']}worker -upgrade <brand> <property>    
    • {theme['g']}worker -info <brand>
    • {theme['g']}worker -list 
    • {theme['g']}worker -sell <brand> <quantity>
    • {theme['g']}worker -exit {theme['w']}: Close the factory
    • {theme['g']}worker -help {theme['w']}: Displays the instructions /guide
    • {theme['g']}worker -usage {theme['w']}: Displays this message
    
    """
    print(usage_text)

def display_guide():
    displayer("--- WORKER FACTORY GUIDE ---", "c", 2)

    help_text = f"""
{theme['y']}COMMAND FORMAT:{theme['w']}
    worker -<action> <arguments>

{theme['y']}COMMANDS:{theme['w']}

{theme['g']}worker -build <brand> <model> <speed_limit> <color>{theme['w']}
    → Create a new car (stock = 1).

{theme['g']}worker -add <brand> <quantity>{theme['w']}
    → Add more cars to stock.

{theme['g']}worker -test <brand>{theme['w']}
    → Run a speed & distance simulation.

{theme['g']}worker -upgrade <brand> <property>{theme['w']}
    → Modify: color, model, speed limit.

{theme['g']}worker -info <brand>{theme['w']}
    → Show car details.

{theme['g']}worker -list{theme['w']}
    → Show all brands.

{theme['g']}worker -sell <brand> <quantity>{theme['w']}
    → Sell cars (updates stock & sold).

{theme['g']}worker -exit{theme['w']}
    → Close factory.

{theme['g']}worker -help{theme['w']}
    → Show this guide.

{theme['g']}worker -usage{theme['w']} or {theme['g']}worker-help -u{theme['w']}
    → Show short usage format.

"""
    print(help_text)

def buildCar(cmd_input:list[str]):
    default_Color = "Black"
    default_speed_limit = 100
    default_model = random.randint(1,3650)
    if(len(cmd_input)<3):
        display_usuage()
    elif(len(cmd_input) == 3):
        Car(cmd_input[2], default_Color, default_model, default_speed_limit)
    elif(len(cmd_input) == 4):
        try:
            converted = int()
            Car(cmd_input[2], cmd_input[3], default_model, default_speed_limit)
        except ValueError as e:
            displayer(f"Error: {e}", "r")
    elif(len(cmd_input) == 5):
        try:
            converted1 = int(cmd_input[3])
            converted2 = int(cmd_input[4])
            Car(cmd_input[2], cmd_input[3], default_model, default_speed_limit)
        except ValueError as e:
            displayer(f"Error: {e}", "r")
    elif(len(cmd_input) == 6):
        try:
            converted1 = int(cmd_input[4])
            converted2 = int(cmd_input[5])
            Car(cmd_input[2],cmd_input[3], converted1, int(cmd_input[5]))
        except ValueError as e:
            displayer(f"Error: {e}", "r")

def getCar(brand_name:str):
    if brand_name.lower() in Car.carsList:
        target_car = Car.carsList[brand_name.lower()] #returns the object stored in carsList dict
        return target_car
    else:
        displayer(f"{brand_name} hasn't been built yet.", "ly")

def ExecCommands(cmd_input):
    action = cmd_input[1]
    match action:
        case "-usuage":
            display_usuage()
        case "-exit":
            displayer("Shutting down the factory. Goodbye :)", "ly")
            os._exit(0)
        case "-build":
            
            buildCar(cmd_input=cmd_input)
        case "-add":
            if(len(cmd_input)==4):
                    theCar = getCar(cmd_input[2])
                    try:
                        qty = int(cmd_input[3])
                    except ValueError as e:
                        displayer("Quantity may have integers only.", "r")
                        return
                    theCar.buildCars(quantity=qty)
            elif(len(cmd_input) <= 3):
                    displayer("Usuage worker -add <brand> <quantity>")
                    return
        case "-help":
            if(len(cmd_input)==3 and cmd_input[2]=="-u"):
                display_usuage()
            else:
                display_guide()
        case "-info":
            if len(cmd_input) == 3:
                try:
                    theCar = getCar(cmd_input[2])
                    theCar.displayInfo()
                except Exception as e:
                    displayer(e,"r")
            else:
                displayer("Not enough arguments: worker -list <brand>\nBrand name missing.", "ly")
                
        case "-upgrade":
            if(len(cmd_input) ==3):
                try:
                    theCar = getCar(cmd_input[2])

                except Exception as e:
                    displayer("Car not found in the factory.", "ly")
                    return
                theCar.upgradeCar()


        case "-sell":
            if(len(cmd_input)==4):
                try:
                    theCar = getCar(cmd_input[2])
                    qty=int(cmd_input[3])
                except ValueError as e:
                    displayer("<quantity> in digits only.", "ly")
                except Exception as e:
                    displayer(e, "ly")
                theCar.sellCars(quantity=qty)
            elif(len(cmd_input) ==2):
                displayer("Missing arguments: <brand> <quantity>","ly")
            elif(len(cmd_input) == 3):
                displayer("Missing arguments: <quantity>", "ly")

        case "-clear":
            print("\033c", end="", flush=True)

        case "-test":
            if len(cmd_input) == 3:
                try:
                    theCar = getCar(cmd_input[2])
                    theCar.testRun()
                except Exception as e:
                    displayer(e,"r")
        case "-list":
            for key,value in Car.carsList.items():
                Car.displayInfo(value)
            else:
                print("-"*30)
        case _:
            displayer(f"Unknown command: '{action}'.\nType 'worker -usuage' for usage.\nType 'worker -help' for the guide/instructions.", "ly")

def main():
    inventory = {}
    
    while True:
        # Prompting the user with a cyan colored'>>'
        cmd_input = input(f"{theme['c']}CarFactory-cli >> {theme['w']}").strip().lower().split()
        
        if not cmd_input:
            continue
        
        cases = cmd_input[0] != "worker" or len(cmd_input)<2
        if(cases):
            display_usuage()
            continue
        ExecCommands(cmd_input=cmd_input)
        
if __name__ == "__main__":
    main()