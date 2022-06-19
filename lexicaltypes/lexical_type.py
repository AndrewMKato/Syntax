class LexicalType:

    def __init__(self, form, label="NULL"):
        self.label = label # NP, N, ...
        self.form = form # Base, past participle, ...
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