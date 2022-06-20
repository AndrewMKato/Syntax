class LexicalType:

    def __init__(self, form: str ="base", label: str ="NULL"):
        self.label = label # Examples: NP, N, ...
        self.form = form # Examples: Base, past participle, ...
        self.valid_forms = {
            'base'
            'past participle' # Eaten, painted, ...
            'present participle' # Eating, painting, ...
        }

        # Tests if form stated is valid.
        try:
            assert self.form in self.valid_forms
        except Exception:
            print('Error: FormNameError')