
from models.gebruiker import Gebruiker
from models.tijd import Tijd
import names as names
import json
import os


class Fietstransporteur(Gebruiker):
    def __init__(self, achternaam, voornaam, tijd_bezig):
        super().__init__(achternaam, voornaam, tijd_bezig)
        self.fietsen = []



class Fietstransporteurs():
    def __init__(self):
        self.fietstransporteurs = []

    def generate_fietstransporteurs(self, aantal_fietstransporteurs):
        data = []
        try:
            for i in range(aantal_fietstransporteurs):
                voornaam = names.get_first_name()
                achternaam = names.get_last_name()
                tijd_bezig = 0
                fietstransporteur = Fietstransporteur(achternaam,voornaam,tijd_bezig)
                self.fietstransporteurs.append(fietstransporteur)
                data.append({
                    'achternaam': achternaam,
                    'voornaam': voornaam,
                    'functie': fietstransporteur.functie,
                    'tijd_bezig': tijd_bezig
                    })
                os.system('cls')
                print(f"generating gebruikers({i}/{aantal_fietstransporteurs})")
                with open(r"dataset_default\fietstransporteurs.json", 'w') as outfile:
                    json.dump(data, outfile)
            return self.fietstransporteurs
        except:
            print("Er heeft zich een probleem voorgedaan bij het wegschrijven naar het uitvoerbestand")

    def save_fietstransporteurs(self):
        data = []
        list = self.fietstransporteurs
        count = 0
        try:
            for key in list:
                gebr = list[count]
                data.append({
                    'achternaam': gebr.achternaam,
                    'voornaam': gebr.voornaam,
                    'functie': gebr.functie,
                    'tijd_bezig': gebr.tijd_bezig
                    })
                count+=1
            with open(r"dataset_save\fietstransporteurs.json", 'w') as outfile:
                outfile.truncate(0)
                json.dump(data, outfile, indent=4)
        except:
            print("Er heeft zich een probleem voorgedaan bij het wegschrijven naar het uitvoerbestand")

    def read_fietstransporteurs(self):
        fileObject = open(r"dataset_save\fietstransporteurs.json", "r")
        jsonContent = fileObject.read()
        fietstransporteurs_bestand = json.loads(jsonContent)
        for fietstr in fietstransporteurs_bestand:
            achternaam = fietstr['achternaam']
            voornaam = fietstr['voornaam']
            tijd_bezig = int(fietstr['tijd_bezig'])
            fietstransporteur = Fietstransporteur(achternaam, voornaam, tijd_bezig)
            self.fietstransporteurs.append(fietstransporteur)
            print(f"reading gebruikers...")
            os.system('cls')
        return self.fietstransporteurs

    def zoek_op_naam(self, naam):
        list = self.fietstransporteurs
        count = 0
        for key in list:
            gebr = list[count]
            gebruiker_full_name = gebr.achternaam +" "+ gebr.voornaam
            if (gebruiker_full_name == naam):
                print("Gebruiker gevonden")
                return gebr
            count+=1