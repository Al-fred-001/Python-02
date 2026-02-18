from typing import Any #importing type Any


'''
To add: 
    the functionality to enumerate items, in a list alone
    the functionality to have sum enumerations (kinda overkill for a print function i guess -_-)
    the functionality to reverse a list as well as the items within it.
'''
def custom_print(*args: Any, 
                sep: str |None = " ",
                end:str|None = "\n",
                caps:bool = False,
                reverse: bool = False,
                include_types: bool = False,
                enumerate: bool = False,
                )->None:
    new_args:list[Any]= []

    #If uppercase enabled conv all strings and strings with list, tuple or set to uppercase. (no change to dict keys, values)
    for arg in args:
        if(isinstance(arg, str) and caps):
            new_args.append(arg.upper())

        elif(caps and isinstance(arg, list|tuple|set)):
            new_list: list[Any] = []
            for value in arg:
                if(isinstance(value, str)):
                    new_list.append(value.upper())
                else:
                    new_list.append(value)
            new_args.append(new_list)
        else:
            new_args.append(arg)
    
    reversed_args: list[Any] = []

    #if reverse is on : reverse items of list, tuple and set, Reverse key-value pairs for dict and reverse the string.
    for arg in new_args:
        if(reverse and not isinstance(arg, dict)):
            reversed(arg)
            reversed_args.append(arg)
        elif(reverse and isinstance(arg, dict)):
            original_dict = arg
            reversed_dict = {value: key for key, value in original_dict.items()}
            reversed_args.append(reversed_dict)
        else:
            reversed_args.append(arg)
        
    type_included_args:list[Any]= []
    #if wants to include types then include it.
    for arg in reversed_args:
        if(include_types):
            type_included_args.append((arg, type(arg)))
        else:
            type_included_args.append(arg)


    enumerated_args: list[Any]= []
    num = 1;
    #if enumerations is desired
    for arg in type_included_args:
        if(enumerate):
            enumed: str = f"{num}. "
            enumed += str(arg)
            enumerated_args.append(enumed)
            num +=1
        else:
            enumerated_args.append(arg)

    all_values:list[Any] = enumerated_args

    #if enumeration = true printing ennumerated list in new line for clear output.
    effective_sep = "\n" if enumerate and sep == " " else sep  
    
    print(*all_values, sep = effective_sep, end= end)
    print("")



#for testing if the function works.
def test()->None:
    aList : list[Any] = ["Alfred", 12, "elepHANt", True,"flask" ]
    custom_print(aList, caps= True)

    aDict : dict[Any, Any]= {
        "name": "al",
        "game": 12,
        "something": True,
        "0": "something"
    }

    custom_print(aDict, reverse = True)

    enumerated: str = "Homer Simpson"
    listed: list[Any] = [1,2,3,4,5,5]
    sets:set = {"a", "a", "b", "C"}


    
    custom_print( enumerated, listed, sets, enumerate=True, include_types=True)


if __name__ == "__main__":
    test()