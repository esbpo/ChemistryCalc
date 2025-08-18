import elementLib as e

def compoundSplit(compound):
    cl = list(compound)
    cl.reverse()
    quantity = 1
    elementLower = ""
    element = ""
    elements = {}
    for i in range(len(cl)):
        if cl[i].isdigit():
            if cl[i-1].isdigit():
                quantity = int(cl[i]+cl[i-1])
            else:
                quantity = int(cl[i])

        if cl[i].islower():
            elementLower = cl[i]

        if cl[i].isupper():
            if elementLower != "":
                element = cl[i] + elementLower
                elementLower = ""
            else:
                element = cl[i]
        
        if element != "":
            if element in elements:
                elements[element] += quantity
            else:
                elements[element] = quantity
            quantity = 1
            element = ""
    return elements

def molarMass(compound):
    elements = compoundSplit(compound)
    total_mass = 0
    if elements != {}:
        for element in elements.keys():
            if element in e.elements:
                atomic_weight = e.elements[element]["atomic_weight"]
                total_mass += atomic_weight * elements[element]
            else:
                return False
        return [compound, total_mass]
    else:
        return False
