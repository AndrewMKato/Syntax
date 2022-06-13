from lexicalCat import Category

class phrase(Category):
    ''' A phrase is composed of a terminal head, a specifier (value of NULL if none present), and any number of complements. '''

    def __init__(self, head, specifier='NULL', *complements,):
        self.head = head
        self.specifier = specifier