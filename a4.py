# returns True if, and only if, string s is a valid variable name
def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

def checkInference(atom, knownAtoms, rules):
    ''' checks if the given atom is infered by the current KB '''
    if atom in rules:
        for i in rules[atom]:
            if i not in knownAtoms:
                return False
        return True
    else:
        return False

def tell(command, atoms, rules):
    ''' tell atom_1 atom_2 ... atom_n:  adds the atoms atom_1 to the current KB
        if atom_i is invalid (according to is_atom), no variables are added '''
    # Error checking
    if len(command) == 1:
        print("Error: tell needs at least one atom")
        return
    
    for i in range(1, len(command)):
        if not is_atom(command[i]):
            print(f"Error: '{command[i]}' is not a valid atom")

    # add atoms into KB
    for i in range(1, len(command)):
        print(command[i] in atoms)
        print(checkInference(command[i], atoms, rules))
        if command[i] in atoms or checkInference(command[i], atoms, rules):
            print(f'    atom "{command[i]}" already known to be true')
        else:
            atoms.append(command[i])
            print(f'    "{command[i]}" added to KB')
    

def infer_all():

    return

def loadKB(command, rules):
    if len(command) != 2:
        print("Error: load can only be used with one argument. Ex) kb> load sample1.txt")
        return

    fileName = command[1]
    if fileName.find(".txt") == -1 or fileName.find(".txt") != len(fileName) - 4:
        print("Error: The KB can only be a textfile (.txt)")
        return
    try:
        f = open(fileName, 'r')
    except:
        print(f"Error: '{fileName}' could not be opened'")
        return
    
    for line in f:
        newRule = line.split()
        # check if line is formatted correctly 
        if len(newRule) != 0:
            rules[newRule[0]] = list(i for i in newRule[2:] if i != '&')

            print(rules[newRule[0]])

    return

def interpreter():
    atomsKnown = []
    atoms = []
    rulesDict = {}
    newAtomsInfered = []
    

    while(1):   
        print("Current atoms:", atoms)
        print("Current Rules:", rulesDict)
        keyboardInput = input("kb> ")
        command = keyboardInput.split()

        if command[0] == "tell":
            tell(command, atoms, rulesDict)

        elif command[0] == "load":
            loadKB(command, rulesDict)

        elif command[0] == "infer_all":
            # command is infer_all

            print("infer_all")

        else:
            print("Error: unknown command", command[0])
            print("Valid commands are 'tell', 'load', and 'infer_all")       

    print("I shouldnt be here")

    return


if __name__ == '__main__':    
    interpreter()