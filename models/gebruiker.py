import names as names
import json
import os

class Gebruiker():
    def __init__(self, achternaam, voornaam, tijd_bezig):
        self.functie = self.__class__.__name__.lower()
        self.achternaam = achternaam
        self.voornaam = voornaam
        self.tijd_bezig = tijd_bezig

    def __repr__(self):
            return f"{self.functie}: {self.achternaam} {self.voornaam} gebruikte tijd: {self.tijd_bezig}"

class Gebruikers():
    def __init__(self):
        self.gebruikers = []

    def generate_gebruikers(self, aantal_gebruikers):
        data = []
        print("generating")
        try:
            for i in range(aantal_gebruikers):
                voornaam = names.get_first_name()
                achternaam = names.get_last_name()
                tijd_bezig = 0
                gebruiker = Gebruiker(achternaam,voornaam,tijd_bezig)
                self.gebruikers.append(gebruiker)
                data.append({
                    'achternaam': achternaam,
                    'voornaam': voornaam,
                    'functie': gebruiker.functie,
                    'tijd_bezig': str(tijd_bezig)
                    })
                print(f"generating gebruikers({i}/{aantal_gebruikers})")
                os.system('cls')
            with open("dataset_default\gebruikers.json", 'w') as outfile:
                json.dump(data, outfile)
            return self.gebruikers
        except:
            print("Er heeft zich een probleem voorgedaan bij het wegschrijven naar het uitvoerbestand")
    
    def save_gebruikers(self):
        data = []
        list = self.gebruikers
        count = 0
        try:
            for key in list:
                gebr = list[count]
                data.append({
                    'achternaam': gebr.achternaam,
                    'voornaam': gebr.voornaam,
                    'functie': gebr.functie,
                    'tijd_bezig': str(gebr.tijd_bezig)
                    })
                count+=1
            with open("dataset_save\gebruikers.json", 'w') as outfile:
                outfile.truncate(0)
                json.dump(data, outfile, indent=4)
        except:
            print("Er heeft zich een probleem voorgedaan bij het wegschrijven naar het uitvoerbestand")
    
    def read_gebruikers(self):
        fileObject = open(r"dataset_save\gebruikers.json", "r")
        jsonContent = fileObject.read()
        gebruikers_bestand = json.loads(jsonContent)
        for gebr in gebruikers_bestand:
            achternaam = gebr['achternaam']
            voornaam = gebr['voornaam']
            tijd_bezig = int(gebr['tijd_bezig'])
            gebruiker = Gebruiker(achternaam, voornaam, tijd_bezig)
            self.gebruikers.append(gebruiker)
            print(f"reading gebruikers...")
            os.system('cls')
        return self.gebruikers

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
