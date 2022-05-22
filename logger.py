class Logger():
    def log_to_file(self, info):
        try:
            output_bestand = open("dataset\log.txt", "w")
        except IOError:
            print("Er was een probleem met het schrijven naar het bestand.")
            quit()

        try:
            output_bestand.write(info)
            output_bestand.close()
        except:
            print("Er heeft zich een probleem voorgedaan bij het wegschrijven naar het uitvoerbestand")
