
# 1 mile = 1.609 km (on this basis)

"""
To add: 
...Thinking
"""



import os
import time

                    # for decoration and other purpose

# for screen clearance : Output clearance
def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux/macOS (posix is the name for non-Windows systems)
        _ = os.system('clear')



#for three dots in loading... and proceeding... etc. 
def threeDots(word: str):
    """
    word => which word to be displayed besides the ... here.
    """
    count = 0
    while(count<2):
        print(f" {word} .    ", end="\r")
        time.sleep(0.25)
        print(f" {word} ..  ", end="\r")
        time.sleep(0.25)
        print(f" {word} ...", end="\r")
        time.sleep(0.25)
        count += 1

def confirmation():
    input("\nPress Enter to continue...") 



                        # Main logic of the program.

MILE_TO_KILOMETERS:float = 1.609  # Km
def main()->int:
    is_running = True

    while (is_running==True):

        #for simple decoration
        threeDots("loading")
        print("---------------------------------------------------------")        


        #Giving option on what user wants to perform.
        print("What do you wish to do? \n\nConvert: \n(1) Miles -> kilometers \n(2) Kilometers -> Miles \n(3) Close the program")
        userInput:int = int(input("\nEnter your response [1-3]: "))


        clear_screen()
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - -") 
        threeDots("Proceeding")
        

        # for matching choice cases
        match userInput:

            # Miles -> kilometers
            case 1:
                data:int = int(input("\nEnter the value (miles) to be converted: "))
                if(data != (-1)):
                    output = data * MILE_TO_KILOMETERS
                    print(f"The value in kilometers is: {output: .3f}")
                    confirmation()
                else: 
                    print("--Invalid entry. Please try again.--")
            

            # kilometers -> miles
            case 2:
                data= int(input("\nEnter the value (Kilometers) to be converted: "))
                if(data != (-1)):
                    output = data / MILE_TO_KILOMETERS
                    print(f"The value in miles is: {output: .3f}")
                    confirmation()
                else: 
                    print("--Invalid entry. Please try again.--")
                    


            # closing the program.
            case 3:
                print("\n--Terminating the program.--\n")
                is_running = False


            #In case of invalid entry.
            case _:
                print("--Invalid entry. Please try again.-")
                
        print()
        print("---------------------------------------------------------")
        # threeDots("Clearing screen")
        clear_screen()

    return 0



if __name__ == "__main__":
    main()