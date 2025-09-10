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
            if not cl[i+1].isupper():
                return False  # Invalid format, lowercase without preceding uppercase

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

def reactionSplit(reaction):
    sides = reaction.split("->")
    if len(sides) != 2:
        return False  # Invalid reaction format
    reactants = sides[0].split("+")
    products = sides[1].split("+")
    reactants = [r.strip() for r in reactants]
    products = [p.strip() for p in products]
    return reactants, products

def koefficientSplit(compound):
    cl = list(compound)
    if len(cl) == 0:
        return False
    else:
        if cl[0].isdigit():
            return (int(cl[0]), compound[1:].strip())
        else:
            return (1, compound.strip())

def molarMass(compound):
    elements = compoundSplit(compound)
    total_mass = 0
    if elements != {} and elements is not False:
        for element in elements.keys():
            if element in e.elements:
                atomic_weight = e.elements[element]["atomic_weight"]
                total_mass += atomic_weight * elements[element]
            else:
                return False
        return [compound, total_mass]
    else:
        return False

def mol(compound, mass):
    molar_mass = molarMass(compound)
    if molar_mass:
        return mass / molar_mass[1]
    else:
        return False
    
def conc(compound, mass, volume):
    moles = mol(compound, mass)
    if moles:
        return moles / volume
    else:
        return False
    
def equality(reaction, molars, Kc=None):
    sides = reactionSplit(reaction)
    compounds = []
    reactants = []
    products = []

    if sides is False:
        return False
    
    if len(molars) != len(sides[0]) + len(sides[1]):
        return False
    if Kc is None:
        for i in range(len(sides)):
            for j in range(len(sides[i])):
                compounds.append(koefficientSplit(sides[i][j]))
                if compounds[-1] is False:
                    return False
                if i == 0:
                    reactants.append((compounds[-1][0], compounds[-1][1], molars.pop(0))) # (coefficient, compound, molar amount)
                elif i == 1:
                    products.append((compounds[-1][0], compounds[-1][1], molars.pop(0))) # (coefficient, compound, molar amount)
    
        Kc = 1
        Kp = 1
        Kr = 1
        for r in reactants:
            if r[2] == 0:
                return False
            Kr *= r[2] ** r[0]
        for p in products:
            if p[2] == 0:
                return False
            Kp *= p[2] ** p[0]
        Kc = Kp / Kr
        return Kc
    else:
        print("Not implemented yet")