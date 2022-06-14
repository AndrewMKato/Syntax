class Sentence:

    def __init__(self, inputSentence='Harvey loves dogs.'):
        self.inputSentence = inputSentence.lower()[:-1]
        self.inputSentence = self.inputSentence.split()

    def __str__(self):
        return str(self.inputSentence)