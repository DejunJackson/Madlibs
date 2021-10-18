class Player:
    def __init__(self, name, words):
        self.name = name
        self.words = words
        self.score = 0
        self.vote = 0

    def __eq__(self, other):
        if (isinstance(other, Player)):
            return self.name == other.name
        return False

    def read_story(self):
        print(
            f"\nOnce upon a time, at a place called {self.words['place']}, there was " +
            f"a {self.words['adjective']} princess named {self.words['femaleName']}.\nHer kingdom " +
            f"was huge, but her {self.words['bodyPart']} was bigger.\nShe was beautiful " +
            f"from her {self.words['bodyPart2']} to her {self.words['organ']}.\nOne day she saw a {self.words['adjective2']} " +
            f"prince named {self.words['maleName']}.\nHe had a {self.words['adjective3']} face. As soon as " +
            f"his {self.words['bodyPart3']} touched her {self.words['bodyPart4']} they fell in love.\nThey " +
            f"got married in {self.words['place2']} the following day.\n")
