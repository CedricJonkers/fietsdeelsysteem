class Fiets():
    def __init__(self, gebruiker, in_gebruik, id):
        self.in_gebruik = in_gebruik
        self.gebruiker = gebruiker
        self.id = id

    def __repr__(self):
        if(self.in_gebruik == True):
            return f"de fiets met id: {self.id} is in gebruik door {self.gebruiker}"
        else:
            return f"de fiets met id: {self.id} is niet in gebruik"
