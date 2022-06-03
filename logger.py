from operator import contains


class Logger():
    def log_to_file(self, info):
        try:
            output_bestand = open("dataset_default\log.txt", "a+")
        except IOError:
            print("Er was een probleem met het schrijven naar het bestand.")
            quit()

        try:
            output_bestand.seek(0)
            data = output_bestand.read(100)
            if(len(data) > 0):
                output_bestand.write("\n")
            output_bestand.write(info)
            output_bestand.close()
        except:
            print("Er heeft zich een probleem voorgedaan bij het wegschrijven naar het uitvoerbestand")
    
    def read_by_name(self, name):
        logs_naam = []
        try:
            with open("dataset_default\log.txt", "r") as bestand:
                for regel in bestand:
                    if regel.find(name) != -1:
                        logs_naam.append(regel)
                return logs_naam
        except FileNotFoundError:
            print("Er is geen data bekend")
            quit()

