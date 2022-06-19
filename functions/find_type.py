from lexicaltypes.terminal_type import TerminalType
import txtfiles

def find_type(word):
    ''' Finds the terminal type of the word given as input. '''

    # nouns.txt file is read into a list.
    with open('nouns.txt', 'r') as f:
        file = f.readlines()

        nouns_file = [i.rstrip() for i in file]

    # names.txt file is read into a list.
    with open('names.txt', 'r') as f:
        file = f.readlines()

        names_file = [i.rstrip().lower() for i in file]

    if word in nouns_file:
        word = TerminalType(label='N')
    elif word in names_file:
        word = TerminalType(label='NAME')
    else:
        word = TerminalType() # word becomes a TerminalType with label value 'NULL'.
        
    return word.label