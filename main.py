import models.gebruiker as gebruiker
import models.fiets as fiets
import models.station as station


class App():
    def __init__(self):
        self.gebruikers_list = gebruiker.Gebruikers()
        self.station = station.Station(0,0)
        self.station_data = station.Stations().read_stations()
        self.gebruikers_data = self.gebruikers_list.generate_gebruikers()


mijn_app = App()
mijn_app.gebruikers_list.toon_gebruikers()
#user = input("Wat is uw naam: ")
#mijn_app.gebruikers_list.zoek_op_naam(user)
#mijn_app.station.voeg_één_fiets_toe(mijn_app.gebruikers_list.zoek_op_naam(user))

# if __name__ == "__main__":
#     main()
