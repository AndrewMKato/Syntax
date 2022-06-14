from lexicalType import LexicalType

class TerminalType(LexicalType):

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
            'pronoun': 'Pron',
            'name': 'Name',
            'NULL': 'NULL'
        }

        # Catch invalid phrasal position or label.
        try:
            assert self.phrasalPosition in self.validPhrasalPositions
        except Exception:
            print(f'Error: PhrasalPositionError')

        try:
            assert self.label in self.validTermLabels.values()
        except Exception:
            print(f'Error: TerminalLabelError')  