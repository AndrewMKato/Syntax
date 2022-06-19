from terminalType import TerminalType

def findType(word):
    ''' Finds the terminal type of the word given as input. '''

    # nouns.txt file is read into a list.
    with open('nouns.txt', 'r') as f:
        file = f.readlines()

        nounsFile = [i.rstrip() for i in file]

    # names.txt file is read into a list.
    with open('names.txt', 'r') as f:
        file = f.readlines()

        namesFile = [i.rstrip().lower() for i in file]

    if word in nounsFile:
        word = TerminalType(label='N')
    elif word in namesFile:
        word = TerminalType(label='Name')
    else:
        word = TerminalType() # word becomes a TerminalType with label value 'NULL'.
        
    return word.label