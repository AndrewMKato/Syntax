from tester import testType

class Sentence:

    def __init__(self, inputSentence='Harvey loves dogs.'):
        self.inputSentence = inputSentence.lower()[:-1]
        self.inputSentence = self.inputSentence.split()


    def __str__(self):
        return str(self.inputSentence)
    
    def associate(self):
        self.inputSentence = {i: None for i in self.inputSentence}

        for i in self.inputSentence:
            i = testType(i)

        return self.inputSentence

        # TODO: Associate each key with the terminalType label associated with it.