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
        command = input("kb> ")
    return


if __name__ == '__main__':    
    interpreter()