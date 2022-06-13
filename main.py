'''
Any given node/constituent consists of
    A lexical category (phrasal or terminal)
    A leaf (the actual word)

Lexical category, which has a leaf 
    Phrase: A head item and its complement items and specifier if any.
    Terminal category: Singular item that is either a head or complement of a phrase.
'''

def main():
    with open('nouns.txt', 'r') as f:
        file = f.readlines()

    nounsFile = [i.rstrip() for i in file]
    


if __name__ == "__main__":
    main()