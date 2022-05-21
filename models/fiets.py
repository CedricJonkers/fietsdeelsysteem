class Fiets():
    def __init__(self, gebruiker, in_gebruik):
        self.in_gebruik = in_gebruik
        self.gebruiker = gebruiker

    def aantal_fietsen():
        with open(r"dataset\velo_data.txt", "r") as elementen_bestand:
            aantal_fietsen = 0
            for element in elementen_bestand:
                element = element.rstrip().split(",")
                if element[13].isnumeric():
                    aantal_fietsen = aantal_fietsen + int(element[13])
            print(aantal_fietsen)

    def __repr__(self):
        return f"Deze fiets word gebruikt door: {self.gebruiker} en is {self.in_gebruik}"
