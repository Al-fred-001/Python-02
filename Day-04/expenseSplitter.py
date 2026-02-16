# expense splitter
import os
print("\n\t-- Expense Splitter --\n")

def main()->None:
    try:
        total_amount:float= float(input("Enter the total amount to be paid: "))
    except ValueError as e:
        print(f"Error: {e}")
        os._exit(2)
    except TypeError as e:
        print(f"Error: {e}")
        os._exit(2)
    except Exception as e:
        print(f"Error: {e}")
        os._exit(2)
    
    people: list[str] = []
    print("...............................................................")
    print("\nAdd participants (Press enter with no input when done): ")
    while True:
        participants_name = input("Add Name: ").strip().capitalize()
        if(participants_name == ""):
            break
        
        if participants_name in people:
            print("\n-- The name is already listed. Please add a different name --")
            continue

        else:
            people.append(participants_name)
    print("...............................................................")

    print("Now, add percentage of the amount to be paid by each person.")
    print('(Type "even" for equal splitting of the bill.)')
    
    print("...............................................................")


    person_dict: dict[str, float] = {}
    total_percentage : float = 100.00
    for person in people:
        print(f"{total_percentage:.0f}% remaining. ")
        input_percentage: str = input(f"Percentage to be paid by {person}: ").strip().lower()

        if (input_percentage == "even"):
            for person in person_dict:
                person_dict[person] = (1/len(people))*total_amount
            break;
        if(input_percentage ==""):
            person_dict[person] = 0.00
            continue

        if(not input_percentage.isdigit()):
            print("Invalid input. Could not proceed.")
            os._exit(2)
            break

        if(float(input_percentage)<=total_percentage ):
            person_dict[person] = (float(input_percentage)/100) * total_amount
            total_percentage -= float(input_percentage)
        else:
            print("Percentage exceeds 100%. Cannot proceed.")
            os._exit(2)
        

    if(total_percentage != 0):
        person_dict["Rest"] = (total_percentage/100)*total_amount
    print("\n--- Split summary ---")
    print("-------------------------------")
    for person, amount in person_dict.items():
        print(f"{person:10}: Rs. {amount:.2f}/-")
    
    print("-------------------------------")

if __name__ == "__main__":
    main()
        
