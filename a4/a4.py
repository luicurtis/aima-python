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

def load(command, rules, isFirstKB):
    ''' loads into memory the KB stored in the file specified in a textfile
        knowledge base file (KB file for short) consists of 1, or more, rules
        require that each rule be written on its own line. Blank spaces are 
        permitted between rules, and extra whitespace is permitted around tokens. 
        Assume that all rules in a KB file have a different head atoms.'''

    # Syntax error checking
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

    atLeastoneRule = False
    for line in f:
        newRule = line.split()
        if len(newRule) != 0:
            atLeastoneRule = True
            ''' Check if each line is formatted correctly before adding into rules
                - check if head is an atom
                - check if <-- comes after the head
                - check if every other char after the <-- is a legal atom
                - check if every char inbetween the atoms are '&'
                - check if all atoms after the <-- are unique
                - check if head is not in the inferring atoms '''
            try:
                if not is_atom(newRule[0]) or newRule[1] != '<--'        \
                    or not all(i == '&' for i in newRule[3::2])          \
                    or not all(is_atom(s) for s in newRule[2::2])        \
                    or not len(set(newRule[2::2])) == len(newRule[2::2]) \
                    or newRule[0] in newRule[2::2]:
                        print("Error", fileName, "is not a valid knowledge base, not formatted correctly")
                        return
            except:
                print("Error", fileName, "is not a valid knowledge base, not formatted correctly")
                return
    
    if not atLeastoneRule: 
        print("Error", fileName, "is not a valid knowledge base, there is not at least 1 rule")
        return

    # Check if a previous KB has been loaded
    if isFirstKB[0]:
        isFirstKB[0] = False
    else:
        # remove previous KB info before adding new rules
        rules.clear()

    f.seek(0)   # set file object postion to the beginning of the file
    # add rules from input KB
    i = 0
    for line in f:
        newRule = line.split()
        if len(newRule) != 0:
            print(f"  {line}", end='')
            rules[newRule[0]] = list(i for i in newRule[2:] if i != '&')
            i += 1

    print(f"\n\n  {i} new rule(s) added")
    return

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
            return

    # add atoms into KB
    for i in range(1, len(command)):
        if command[i] in atoms:
            print(f'  atom "{command[i]}" already known to be true')
        elif command[i] in rules.keys() and not checkInference(command[i], atoms, rules):
            print(f'Error: Cannot tell {command[i]} because it is a head of a definite clause and cannot be proven yet')
        else:
            atoms.append(command[i])
            print(f'  "{command[i]}" added to KB')
    return

def infer_all(rules, atoms):
    ''' Prints all the atoms that can currently be inferred by the rules in the KB. 
        Note that no atoms can be inferred until at least one tell command is called. '''
    
    inferedList = []
    heads = rules.keys()
    newInference = True

    # keep looping until no new inferences were found
    while (newInference):
        newInference = False
        for head in heads:
            allAtoms = set(atoms + inferedList)     # allAtoms will always include all new infered atoms
            if all(atom in allAtoms for atom in rules[head]) and \
                    (head not in allAtoms):
                inferedList.append(head)
                newInference = True
    return inferedList


def interpreter():
    atoms = []
    rulesDict = {}
    firstKBFlag = [True]  # need a mutable type to be changed in the calling function

    # interpreter should never crash: any error should just cause a helpful error message to be printed.
    while(1):
        keyboardInput = input("kb> ")
        command = keyboardInput.split()
        if len(command) == 0:
            print("Error: No command inputted. Valid commands are 'tell', 'load', and 'infer_all")
        elif command[0] == "tell":
            tell(command, atoms, rulesDict)
        elif command[0] == "load":
            load(command, rulesDict, firstKBFlag)
        elif command[0] == "infer_all":
            newlyInfered = infer_all(rulesDict, atoms)
            print("  Newly inferred atoms:")
            print("    ", end='')
            if len(newlyInfered) == 0:
                print("<none>")
            else:
                print(*newlyInfered, sep=', ')

            print("  Atoms already known to be true:")
            print("    ", end='')
            if len(atoms) == 0:
                print("<none>")
            else:
                print(*atoms, sep=', ')

            for newAtom in newlyInfered:
                atoms.append(newAtom)
        else:
            print("Error: unknown command", command[0])
            print("Valid commands are 'tell', 'load', and 'infer_all")
    return

if __name__ == '__main__':
    interpreter()