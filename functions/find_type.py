from lexicaltypes.terminal_type import TerminalType

def find_type(word):
    ''' Finds the terminal type of the word given as input. '''

    # Each file is read into a respective list.
    with open('nouns.txt', 'r') as f:
        file = f.readlines()
        nouns_file = [i.rstrip() for i in file]

    with open('names.txt', 'r') as f:
        file = f.readlines()
        names_file = [i.rstrip().lower() for i in file]

    with open('adjectives.txt', 'r') as f:
        file = f.readlines()
        adjectives_file = [i.rstrip().lower() for i in file]

    if word in nouns_file:
        word = TerminalType(label='N')
    elif word in names_file:
        word = TerminalType(label='NAME')
    elif word in adjectives_file:
        word = TerminalType(label='A')
    else:
        word = TerminalType() # word becomes a TerminalType with label 'NULL'.
        
    return word.label