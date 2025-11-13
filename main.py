import sys
sys.path.append(".lib")
import funcLib as f # type: ignore
import elementLib as e # type: ignore
import SIConvertLib as SI # type: ignore
import math

quit = False
exit_commands = ["quit", "exit"]
print("Enter 'help' for a list of commands.")

while not quit:
    userInput = input("> ").strip().split()
    if len(userInput) > 0:
        userInput[0] = userInput[0].lower()
    else:
        continue

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
            print("6. convert <value> <unit> - Convert a given value in a given unit to either meters, grams, seconds or liters")
            print("7. concentration <compound> <mass_in_grams> <volume_in_liters> - Calculate the concentration in mol/L of a given mass of a compound in a given volume.")
            print("8. density <mass_in_grams> <volume_in_liters> - Calculate the density in g/L of a given mass in a given volume.")
            print("9. equality <OPTIONS> <reaction> <molar1> <molar2> ... - Calculate the equality constant of a given reaction with the molars of the substances.")
            print("10. ph <known_factor1> <value1> <known_factor2> <value2>... - Calculate pH, known_factors: -n (moles), -v (volume), -c (concentration)")
            print("?. quit/exit - Exit the program.")
        else:
            if userInput[1] == "molarmass":
                print("Usage: molarMass <compound>\nCalculates the molar mass of a given chemical compound. Example: molarMass H2O > 18.015 g/mol")
            elif userInput[1] == "split":
                print("Usage: split <compound> <info>\nSplits a chemical compound into its constituent elements and their quantities.\nWrites element info if 'info' is given. Example: split CH3CH2COOH > H: 6, O: 2, C: 3")
            elif userInput[1] == "info":
                print("Usage: info <element_symbol> - Get information about a specific element. Example: info Ca > Name: Calcium, Atomic Number: 20, Atomic Weight: 40.078 g/mol},")
            elif userInput[1] == "mol":
                print("Usage: mol <compound> <mass_in_grams> - Calculate the number of moles in a given mass of a compound. Example: mol H2O 18.015 > 1 mol")
            elif userInput[1] == "concentration":
                print("Usage: concentration <compound> <mass_in_grams> <volume_in_liters> - Calculate the concentration in mol/L of a given mass of a compound in a given volume. Example: concentration H2O 18.015 1 > 1 mol/L")
            elif userInput[1] == "density":
                print("Usage: density <mass_in_grams> <volume_in_liters> - Calculate the density in g/L of a given mass in a given volume. Example: density 1000 1 > 1000 g/L")
            elif userInput[1] == "convert":
                print("Usage: convert <value> <unit> - Convert a given value in a given unit to either meters, grams, seconds or liters. Example: convert 100 cm > 1 m")
                print("Write 'help units' for a list of available units.")
            elif userInput[1] == "equality":
                print("Usage: equality <OPTIONS> <reaction> <molar1> <molar2> - Calculate the equality constant of a given reaction with the molars of the substance. DO NOT USE")
                print("Available options: -k <equality_constant>")
            elif userInput[1] == "ph":
                print("Usage: ph <known_factor1> <value1> <known_factor2> <value2>... - Calculate pH, known_factors: -n (moles), -v (volume), -c (concentration). Example: ph -c 0.1 > 1")
            elif userInput[1] == "units":
                SI.printUnits()

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

    elif userInput[0] == "concentration":
        if len(userInput) == 4:
            try:
                mass = float(userInput[2])
                volume = float(userInput[3])
                out = f.conc(userInput[1], mass, volume)
                if out:
                    print(f"The concentration of {mass}g of {userInput[1]} in {volume}L is {out} mol/L.")
                else:
                    print(f"Compound {userInput[1]} contains elements not found in the periodic table.")
            except ValueError:
                print("Please provide valid mass in grams and volume in liters.")

    elif userInput[0] == "density":
        if len(userInput) == 3:
            try:
                mass = float(userInput[1])
                volume = float(userInput[2])
                if volume <= 0:
                    print("Volume must be greater than zero.")
                else:
                    density = mass / volume
                    print(f"The density of the substance is {density} g/L.")
            except ValueError:
                print("Please provide valid mass in grams and volume in L.")

    elif userInput[0] == "convert":
        if len(userInput) == 3:
            try:
                unit = userInput[2]
                value = float(userInput[1])
                out = SI.convert_to_si(value, unit)
                if out:
                    print(f"{value} {unit} is equivalent to {out[0]} {out[1]}")
                else:
                    print("Please give a valid unit, write 'help units' for list")
            except ValueError:
                print("Value not valid")

    elif userInput[0] == "equality":
        if len(userInput) >= 3:
            if userInput[1] == "-k":
                try:
                    eqConst = float(userInput[2])
                except ValueError:
                    print("Please provide a valid equality constant.")
                    continue
                reaction = userInput[3]
                molars = []
                for i in range(4, len(userInput)):
                    try:
                        molars.append(float(userInput[i]))
                    except ValueError:
                        print(f"Molar value {userInput[i]} is not a valid number.")
                        break
                out = f.equality(reaction, molars, eqConst)
                if out:
                    print(f"The equality constant for the reaction: {reaction} is {out}.")
                else:
                    print("Error calculating the equality constant. Please check the reaction format and molar values.")
            else:
                reaction = userInput[1]
                molars = []
                for i in range(2, len(userInput)):
                    try:
                        molars.append(float(userInput[i]))
                    except ValueError:
                        print(f"Molar value {userInput[i]} is not a valid number.")
                        break
                out = f.equality(reaction, molars)
                if out:
                    print(f"The equality constant for the reaction: {reaction} is {out}.")
                else:
                    print("Error calculating the equality constant. Please check the reaction format and molar values.")
        else:
            print("Usage: equality <OPTIONS> <reaction> <molar1> <molar2> ...")

    elif userInput[0] == "ph":
        known_factors = {}
        for i in range(len(userInput)):
            item = userInput[i]
            if item == "-c":
                known_factors["-c"] = float(userInput[i+1])
            elif item == "-n":
                known_factors["-n"] = float(userInput[i+1])
            elif item == "-v":
                known_factors["-v"] = float(userInput[i+1])
        
        if "-c" in known_factors.keys():
            pH = -1 * math.log10(known_factors["-c"])
            print(f"The pH of the concentration {known_factors['-c']} moles/liter is {pH}")
        elif "-n" in known_factors.keys() and "-v" in known_factors.keys():
            pH = -1 * math.log10(known_factors["-n"]/known_factors["-v"])
            print(f"The pH of {known_factors['-n']} moles in {known_factors['-v']} liter is {pH}")
        else:
            print("Something is missing from your command.")
            print("Usage: pH <know factor 1> <value 1> <know factor 2> <value 2>")
    
    elif userInput[0] in exit_commands:
        quit = True
        print("Quitting...")