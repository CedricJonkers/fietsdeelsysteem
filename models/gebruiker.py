import names as names
import json

class Gebruiker():
    def __init__(self, achternaam, voornaam):
        self.functie = self.__class__.__name__.lower()
        self.achternaam = achternaam
        self.voornaam = voornaam

    def __repr__(self):
        return f"{self.functie}: {self.achternaam} {self.voornaam}"

class Gebruikers():
    def __init__(self):
        self.gebruikers = []

    def generate_gebruikers(self):
        data = []
        try:
            for i in range(100):
                voornaam = names.get_first_name()
                achternaam = names.get_last_name()
                gebruiker = Gebruiker(achternaam,voornaam)
                self.gebruikers.append(gebruiker)
                data.append({
                    'achternaam': achternaam,
                    'voornaam': voornaam,
                    'functie': gebruiker.functie,
                    })
                with open("dataset\gebruikers.json", 'w') as outfile:
                    json.dump(data, outfile)
            return self.gebruikers
        except:
            print("Er heeft zich een probleem voorgedaan bij het wegschrijven naar het uitvoerbestand")

    def zoek_op_naam(self, naam):
        list = self.gebruikers
        count = 0
        for key in list:
            gebr = list[count]
            gebruiker_full_name = gebr.achternaam +" "+ gebr.voornaam
            if (gebruiker_full_name == naam):
                print("Gebruiker gevonden")
                return gebr
            count+=1

    def toon_gebruikers(self):
        list = self.gebruikers
        count = 0
        for key in list:
            gebr = list[count]
            print(gebr)
            count+=1
        return list
            

    def __repr__(self):
        return '\n'.join(str(gebr) for gebr in self.gebruikers)
