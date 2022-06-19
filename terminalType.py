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
            'degree': 'DEG',
            'negation': 'NEG',
            'possessive': 'POSS',
            'pronoun': 'PROM',
            'name': 'NAME',
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