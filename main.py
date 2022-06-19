'''
This parser focuses on general constituent identification.
Attention will be primarily given to finding and labeling phrasal constituents, i.e. NPs, VPs, etc.

A sentence has phrasal constituents (phrases).
Phrases have terminal constituents (individual words).
Both phrases and terminal constituents should subclasses of a constituent superclass.
'''

from sentence import Sentence

def main():
    input_sentence = Sentence(input('Enter a sentence for parsing: ')) # ['harvey', 'loves', 'dogs']
    print(input_sentence)

    input_sentence = input_sentence.associate() # {'harvey': 'Name', 'loves': 'NULL', 'dogs': 'NULL'}
    print(input_sentence) 







if __name__ == "__main__":
    main()

    # GOAL: Harvey loves dogs. -> [(NP) N.Harvey] [(M') M.NULL [(VP) V.loves [(NP) N.dogs]]].

    # GOAL: The green goblin loves eating apples. -> [(NP) [(DP) D.The [AP A.green]] N.goblin] [(M') M.NULL [(VP) V.loves [(VP) V.eating [(NP) N.apples]]]].