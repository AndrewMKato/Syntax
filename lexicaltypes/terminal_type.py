from lexicaltypes.lexical_type import LexicalType

class TerminalType(LexicalType):

    def __init__(self, phrasal_position='complement', label='NULL'):
        self.label = label
        self.phrasal_position = phrasal_position
        
        self.valid_phrasal_positions = ['complement', 'head', 'specifier']
        self.valid_term_labels = {
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
            assert self.phrasal_position in self.valid_phrasal_positions
        except Exception:
            print('Error: PhrasalPositionError')

        try:
            assert self.label in self.valid_term_labels.values()
        except Exception:
            print('TerminalLabelError')
            #print(self.valid_term_labels.values())
            print(f'Error: TerminalLabelError. self.label = {self.label}')  