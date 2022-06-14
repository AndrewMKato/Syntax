from lexicalType import LexicalType

class terminalType(LexicalType):

    def __init__(self, phrasalPosition='complement', label='NULL'):
        self.label = label
        self.phrasalPosition = phrasalPosition
        
        self.validPhrasalPositions = ['complement', 'head', 'specifier']
        self.validTermLabels = {
            'noun': 'N',
            'verb': 'V',
            'adjective': 'A',
            'determiner': 'D',
            'complementizer': 'C',
            'preposition': 'P',
            'degree': 'Deg',
            'negation': 'Neg',
            'possessive': 'Poss',
            'pronoun': 'Pron'
        }

        # Catch invalid phrasal position or label.
        try:
            assert self.phrasalPosition in self.validPhrasalPositions

        except Exception as PhrasalPositionError:
            print(f'Error: {PhrasalPositionError}')

        try:
            assert self.label in self.validTermLabels

        except Exception as LabelError:
            print(f'Error: {LabelError}')

        
            