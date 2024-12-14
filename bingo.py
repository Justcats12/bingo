import random

DEFAULT_SIZE = 16

class Bingo():
    def __init__(self, array = [], filename = "", size = DEFAULT_SIZE):
        self.options : list = array
        
        if filename != "":
            self.getFromFile(filename=filename)

        assert len(self.options) >= DEFAULT_SIZE, "Bingo isn't big enough"
    
    def __repr__(self):
        return f"bingo{self.options}"

    def getBingo(self):
        """Generate the options for a random bingo card in a list"""
        bingoOptions = self.options.copy()
        random.shuffle(bingoOptions)
        return bingoOptions[:DEFAULT_SIZE]
    
    def getFromFile(self, filename):
        bingoFile = open(filename, "r")
        lines = bingoFile.readlines()

        self.options = [ l.strip() for l in lines ]

