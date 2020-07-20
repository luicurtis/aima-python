# returns True if, and only if, string s is a valid variable name
def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

def tell():

    return

def infer_all():

    return

def loadKB():

    return

def interpreter():
    while(1):   
        keyboardInput = input("kb> ")
        
        command = keyboardInput.split()
        if command[0] != "tell" and command[0] != "load" and command[0] != "infer_all":
            print("Error: unknown command", command[0])
            print("Valid commands are 'tell', 'load', and 'infer_all")
            continue;
        
        print("here")

    print("i dont want to be here")

    return


if __name__ == '__main__':    
    interpreter()