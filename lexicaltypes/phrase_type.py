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
            'modal': 'M',
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
            print(f'Error: TerminalLabelError. self.label = {self.label}')  

class PhraseType(LexicalType):
    ''' A phrase is composed of a terminal head, a specifier (value of NULL if none present), and any number of complements. '''

    def __init__(self, head: TerminalType, specifier: TerminalType('specifier'), *complements: (TerminalType)):
        self.head = head
        self.specifier = specifier
        self.complements = complements # Currently of type tuple.