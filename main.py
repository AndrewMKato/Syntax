'''
Any given constituent consists of
    A lexical type (phrasal or terminal)
    A leaf (the actual word)

Lexical type
    Phrase: A head item and its complement items and specifier if any.
    Terminal type: Singular item that is either a head or complement of a phrase.
'''

from sentence import Sentence

def main():
    inputSentence = Sentence(input('Enter a sentence for parsing: ')) # ['harvey', 'likes', 'dogs']
    print(inputSentence) # Returns str.

if __name__ == "__main__":
    main()

    # Harvey likes dogs. -> "[(NP) [(N) Harvey]] [(VP) [(V) likes] [(N) dogs]]