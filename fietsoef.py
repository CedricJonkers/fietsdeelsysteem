class Gebruiker():
    def __init__(self, achternaam, naam, bezig):
        self.achternaam = achternaam
        self.naam = naam
        self.bezig = bezig

    def __repr__(self):
        return f"{self.achternaam} {self.naam}"


class Slot():
    def __init__(self, nummer, bezet):
        self.nummer = nummer
        self.bezet = bezet

    def __repr__(self):
        return f"Slot nr: {self.nummer} is {self.bezet}"


class Fiets():
    def __init__(self, in_gebruik):
        self.in_gebruik = in_gebruik


class Station():
    def __init__(self):
        self.aantal_slots = []
        self.aantal_fietsen = []
        self.aantal_gebruikers = []

    def voeg_fiets_toe(self, fiets, gebruiker, slot):
        self.aantal_fietsen.append(fiets)

