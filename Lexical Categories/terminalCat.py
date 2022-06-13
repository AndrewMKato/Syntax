from lexicalCat import Category

class terminalCategory(Category):

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

        # Catches invalid label or phrasal position.
        try:
            assert self.phrasalPosition in self.validPhrasalPositions

        except Exception as phrasalPositionError:
            print(f'Error: {phrasalPositionError}')

        try:
            assert self.label in self.validTermLabels

        except Exception as labelError:
            print(f'Error: {labelError}')

        
            