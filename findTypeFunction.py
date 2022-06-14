from terminalType import TerminalType

def findType(word):

    with open('nouns.txt', 'r') as f:
        file = f.readlines()

        nounsFile = [i.rstrip() for i in file]

    with open('names.txt', 'r') as f:
        file = f.readlines()

        namesFile = [i.rstrip().lower() for i in file]

    if word in nounsFile:
        word = TerminalType(label='N')
    elif word in namesFile:
        word = TerminalType(label='Name')
    else:
        word = TerminalType()
        
    return word.label