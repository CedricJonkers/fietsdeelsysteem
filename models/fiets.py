class Fiets():
    def __init__(self, gebruiker, in_gebruik):
        self.in_gebruik = in_gebruik
        self.gebruiker = gebruiker

    def __repr__(self):
        if(self.in_gebruik == True):
            return f"deze fiets is in gebruik door {self.gebruiker},{self.in_gebruik}"
        else:
            return f"deze fiets is niet in gebruik {self.in_gebruik}"
