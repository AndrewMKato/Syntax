def testType(word):
    with open('nouns.txt', 'r') as f:
        file = f.readlines()

        nounsFile = [i.rstrip() for i in file]

    if word in nounsFile:
        pass