import sys
sys.path.append(".lib")
import funcLib as f # type: ignore
import elementLib as e # type: ignore

quit = False
exit_commands = ["quit", "exit"]
print("Enter 'help' for a list of commands.")

while not quit:
    userInput = input("> ").strip().split()
    userInput[0] = userInput[0].lower()

    if userInput[0] == "molarmass":
        if len(userInput) == 2:
            out = f.molarMass(userInput[1])
            if out:
                print(f"The molar mass of {out[0]} is {out[1]} g/mol")
            else:
                print(f"Compound {userInput[1]} contains elements not found in the periodic table.")
        else:
            print("Usage: molarMass <compound>")

    elif userInput[0] == "split":
        if len(userInput) >= 2:
            elements = f.compoundSplit(userInput[1])
            for element, quantity in elements.items():
                if element in e.elements:
                    if len(userInput) > 2 and userInput[2] == "info":
                        print(f"{element}: {quantity} (Name: {e.elements[element]['name']}; Atomic Number: {e.elements[element]['atomic_number']}; Atomic Weight: {e.elements[element]['atomic_weight']} g/mol)")
                    else:
                        print(f"{element}: {quantity}")
                else:
                    print(f"Element {element} not found in the periodic table.")
        else:
            print("Usage: split <compound>")

    elif userInput[0] == "help":
        if not userInput[1:]:
            print("Available commands:")
            print("1. molarMass <compound> - Calculate the molar mass of a compound.")
            print("2. split <compound> <info> - Split a compound into its constituent elements and their quantities. Display info if 'info' is provided.")
            print("3. info <element_symbol> - Get information about an element.")
            print("4. help <command> - Get help on a specific command, if left blank show this message.")
            print("5. mol <compound> <mass_in_grams> - Calculate the number of moles in a given mass of a compound.")
            print("?. quit/exit - Exit the program.")
        else:
            if userInput[1] == "molarmass":
                print("Usage: molarMass <compound>\nCalculates the molar mass of a given chemical compound. Example: molarMass H2O = 18.015 g/mol")
            elif userInput[1] == "split":
                print("Usage: split <compound> <info>\nSplits a chemical compound into its constituent elements and their quantities.\nWrites element info if 'info' is given. Example: split CH3CH2COOH = H: 6, O: 2, C: 3")

    elif userInput[0] == "info":
        if len(userInput) == 2:
            if userInput[1] in e.elements:
                element = e.elements[userInput[1]]
                print(f"Name: {element["name"]}\nAtomic Number: {element["atomic_number"]}\nAtomic Weight: {element["atomic_weight"]} g/mol")
            else:
                print(f"Element {userInput[1]} not found in the periodic table.")
        else:
            print("Usage: info <element_symbol>")

    elif userInput[0] == "mol":
        if len(userInput) == 3:
            try:
                mass = float(userInput[2])
                out = f.mol(userInput[1], mass)
                if out:
                    print(f"{userInput[2]} g of {userInput[1]} is {out} mol(s).")
                else:
                    print(f"Compound {userInput[1]} contains elements not found in the periodic table.")
            except ValueError:
                print("Please provide a valid mass in grams.")
        else:
            print("Usage: mol <compound> <mass_in_grams>")
    
    elif userInput[0] in exit_commands:
        quit = True
        print("Quitting...")