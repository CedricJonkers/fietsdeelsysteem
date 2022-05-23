import models.fietstransporteur as fietstransporteur
import models.gebruiker as gebruiker
import models.fiets as fiets
import models.station as station
import sys, os
import pandas as pd
import html_writer as html_writer


class App():
    def __init__(self):
        self.gebruikers_list = gebruiker.Gebruikers()
        self.fietstransporteurs_list = fietstransporteur.Fietstransporteurs()
        self.station = station.Station(0, "Baron Sadoinestraat (2660)","",0,0,0)
        self.stations = station.Stations()
        self.station_data = self.stations.read_stations()
        self.gebruikers_data = self.gebruikers_list.generate_gebruikers()
        self.fietstransporteurs_data = self.fietstransporteurs_list.generate_fietstransporteurs()


mijn_app = App()
mijn_app.stations.add_slots_bikes(mijn_app.fietstransporteurs_data)

#os.system('cls')
option_menu = {
    1: 'Toon gebruikers',
    2: 'Toon stations',
    3: 'check slots',
    4: 'neem fiets',
    5: 'voeg fiets toe',
    6: 'check fietsen',
    7: 'verplaats fietsen',
    8: 'generate html',
    9: 'exit'
}


def print_options():

    for x in range(90):
        print("-", end="")
    print("Welcome to A-velo", end= "")
    for x in range(90):
        print("-", end="")
    for key in option_menu.keys():
        print('|',key, '---', option_menu[key])
    for x in range(197):
        print("-", end="")

while(True):
    print_options()
    option = ""

    try:
        option = int(input('\nEnter option: '))

    except:
        print("option", option, "\n")

    if option == 1:
        list_g = mijn_app.gebruikers_list.toon_gebruikers()

    elif option == 2:
        list_s = mijn_app.stations.toon_stations()

    elif option == 3:
        stat = input('Geef je station: ')
        mijn_station = mijn_app.stations.zoek_op_id(stat)
        print(mijn_station.check_slot())
        
    elif option == 4:
        naam = input('Geef je naam: ')
        user = mijn_app.gebruikers_list.zoek_op_naam(naam)
        if(mijn_app.gebruikers_list.zoek_op_naam(naam) != None):
          stat = int(input('Geef je station id: '))
          mijn_station = mijn_app.stations.zoek_op_id(stat)
          print("Beste", naam, mijn_station.geef_fiets(user), ", je mag deze gebruiken.")

    elif option == 5:
        gebr = input('Geef je naam: ')
        user = mijn_app.gebruikers_list.zoek_op_naam(gebr)
        print(user)
        if(mijn_app.gebruikers_list.zoek_op_naam(gebr) != None):
          stat = input('Geef je station: ')
          mijn_station = mijn_app.stations.zoek_op_id(stat)
          slot = input('Geef het slot nummer: ')
          mijn_station.voeg_plaats_toe(slot)
          mijn_app.stations.verwijder_fiets(user)
        else:
          print("Naam bestaat niet")

    elif option == 6:
        stat = input('Geef je station: ')
        mijn_station = mijn_app.stations.zoek_op_id(stat)
        print(mijn_station.check_fiets())

    elif option == 7:
        naam = input("Geef je naam: ")
        transporteur = mijn_app.fietstransporteurs_list.zoek_op_naam(naam)
        teveel = mijn_app.stations.check_teveel_fietsen()
        teweinig = mijn_app.stations.check_teweinig_fietsen()
        fietsen = mijn_app.stations.zet_fietsen_in_wagen(teveel, transporteur)
        mijn_app.stations.zet_fietsen_in_nieuw_station(fietsen,teweinig)

    elif option == 8:
        stat = input('Geef je station: ')
        mijn_station = mijn_app.stations.zoek_op_id(stat)
        print(mijn_station.check_fiets())
        h = html_writer.htmlWriter()
        df = pd.DataFrame({'slots':mijn_station.check_slot()})
        print(df)
        html_table = h.create_html_table(df)
        print(html_table)
        h.create_html_page(html_table, df, mijn_station.id)

    elif option == 9:
        print("Exit code....")
        exit()
    else:
        print('invalid option:', option, 'Try again...')


# if __name__ == "__main__":
#     main()
