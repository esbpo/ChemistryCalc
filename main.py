import funcLib as f
import elementLib as e

userInput = input("").strip().split()
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
    if len(userInput) == 2:
        elements = f.compoundSplit(userInput[1])
        for element, quantity in elements.items():
            if element in e.elements:
                print(f"{element}: {quantity} (Atomic Weight: {e.elements[element]['atomic_weight']} g/mol)")
            else:
                print(f"Element {element} not found in the periodic table.")
    else:
        print("Usage: split <compound>")

elif userInput[0] == "help":
    print("Available commands:")
    print("1. molarMass <compound> - Calculate the molar mass of a compound.")
    print("2. split <compound> - Split a compound into its constituent elements and their quantities.")

elif userInput[0] == "info":
    if len(userInput) == 2:
        if userInput[1] in e.elements:
            element = e.elements[userInput[1]]
            print(f"Name: {element["name"]}\nAtomic Number: {element["atomic_number"]}\nAtomic Weight: {element["atomic_weight"]} g/mol")
        else:
            print(f"Element {userInput[1]} not found in the periodic table.")
    else:
        print("Usage: info <element_symbol>")