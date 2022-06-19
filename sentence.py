from functions.find_type import find_type

class Sentence:

    def __init__(self, input_sentence: str):

        # input_sentence is a list of the words, in lowercase, of the input sentence provided.
        self.input_sentence = input_sentence.lower()[:-1] # The period is deleted.
        self.input_sentence = self.input_sentence.split()

    def __str__(self):
        ''' Using print() on a sentence will return a string version of the self.input_sentence list.'''

        return str(self.input_sentence)
    
    def associate(self):
        ''' Associates each word with their respective lexical category by using the find_type() function.'''

        # self.input_sentence becomes a dictionary. Each word is given the automatic value of 'NULL'.
        self.input_sentence = {i: 'NULL' for i in self.input_sentence}

        # Using find_type, each key takes on the value of its respective lexical category.
        for i in self.input_sentence:
            self.input_sentence[i] = find_type(i)

        return self.input_sentence