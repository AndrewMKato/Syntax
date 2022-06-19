from findTypeFunction import findType

class Sentence:

    def __init__(self, inputSentence='Harvey loves dogs.'):
        self.inputSentence = inputSentence.lower()[:-1] # All words become lowercase and the period is deleted.
        self.inputSentence = self.inputSentence.split() # String is split into a list, with each word as an element.

    def __str__(self):
        return str(self.inputSentence)
    
    def associate(self):
        ''' Method of the Sentence class. Associates each word with their respective terminal type by using the findType() function.'''

        self.inputSentence = {i: 'NULL' for i in self.inputSentence}
        for i in self.inputSentence:
            self.inputSentence[i] = findType(i)

        return self.inputSentence

    def 