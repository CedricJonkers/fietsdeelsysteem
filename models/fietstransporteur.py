
from models.gebruiker import Gebruiker
import names as names
import json


class Fietstransporteur(Gebruiker):
    def __init__(self, achternaam, voornaam):
        super().__init__(achternaam, voornaam)



class Fietstransporteurs():
    def __init__(self):
        self.fietstransporteurs = []
    def generate_fietstransporteurs(self):
        data = []
        try:
            for i in range(10):
                voornaam = names.get_first_name()
                achternaam = names.get_last_name()
                fietstransporteur = Fietstransporteur(achternaam,voornaam)
                self.fietstransporteurs.append(fietstransporteur)
                data.append({
                    'achternaam': achternaam,
                    'voornaam': voornaam,
                    'functie': fietstransporteur.functie
                    })
                with open(r"dataset\fietstransporteurs.json", 'w') as outfile:
                    json.dump(data, outfile)
            return self.fietstransporteurs
        except:
            print("Er heeft zich een probleem voorgedaan bij het wegschrijven naar het uitvoerbestand")

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