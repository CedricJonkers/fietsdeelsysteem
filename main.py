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
        aantal_gebruikers = int(input('Hoeveel gebruikers wilt u: '))
        self.gebruikers_data = self.gebruikers_list.generate_gebruikers(aantal_gebruikers)
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
    9: 'simulatie',
    10: 'save',
    11: 'exit'
}

sub_option_menu = {
    1: 'Fiets',
    2: 'Gebruiker',
    3: 'Station'
}


def print_options(y, tekst):
    size = os.get_terminal_size()
    print(size.columns)
    for x in range(round(size.columns/2)):
        print("-", end="")
    print(tekst, end= "")
    for x in range(round(size.columns/2 - len(tekst))):
        print("-", end="")
    for key in y.keys():
        print('|',key, '---', y[key])
    for x in range(size.columns):
        print("-", end="")

while(True):
    print_options(option_menu,"Welcome to A-velo")
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
        if(mijn_app.gebruikers_list.zoek_op_naam(naam) != None and mijn_app.stations.check_fiets_gebruiker(user) != True):
          stat = int(input('Geef je station id: '))
          if (mijn_app.stations.zoek_op_id(stat) != None and mijn_app.stations.zoek_op_id(stat).check_slot_met_fiets() != 0):
              mijn_station = mijn_app.stations.zoek_op_id(stat)
              print("Beste", naam, mijn_station.geef_fiets(user,mijn_app.stations), ", je mag deze gebruiken.")
          else:
              print("dit station heeft geen fietsen meer of bestaat niet")
        else:
            print("Je hebt al een fiets")

    elif option == 5:
        gebr = input('Geef je naam: ')
        user = mijn_app.gebruikers_list.zoek_op_naam(gebr)
        if(mijn_app.gebruikers_list.zoek_op_naam(gebr) != None):
          stat = input('Geef je station: ')
          mijn_station = mijn_app.stations.zoek_op_id(stat)
          slot = input('Geef het slot nummer: ')
          id = mijn_app.stations.check_fiets_gebr(user)
          mijn_station.voeg_plaats_toe(slot, id)
          mijn_app.stations.verwijder_fiets(user, mijn_station)
        else:
          print("Naam bestaat niet")

    elif option == 6:
        stat = input('Geef je station: ')
        mijn_station = mijn_app.stations.zoek_op_id(stat)
        print(mijn_station.check_fiets_station())

    elif option == 7:
        naam = input("Geef je naam: ")
        transporteur = mijn_app.fietstransporteurs_list.zoek_op_naam(naam)
        teveel = mijn_app.stations.check_teveel_fietsen()
        teweinig = mijn_app.stations.check_teweinig_fietsen()
        print(teveel)
        print(teweinig)
        fietsen = mijn_app.stations.zet_fietsen_in_wagen(teveel, transporteur)
        print(fietsen)
        mijn_app.stations.zet_fietsen_in_nieuw_station(fietsen,teweinig, transporteur)
        print(teweinig)

    elif option == 8:
        print_options(sub_option_menu,"Van welk onderdeel wil je een beeld krijgen")
        option = ""
        try:
            option = int(input('\nEnter option: '))
        except:
            print("option", option, "\n")
        if option == 1:
            fie_id = int(input('Geef je fietsid: '))
            fie = mijn_app.stations.check_fiets(fie_id)
            df = pd.DataFrame({'fiets':[fie]})
            html_table = html_writer.htmlWriter().create_html_table(df)
            html_writer.htmlWriter().create_html_page(html_table, df, fie.id)
        elif option == 2:
                gebr = input('Geef je naam: ')
                user = mijn_app.gebruikers_list.zoek_op_naam(gebr)
                df = pd.DataFrame({'gebruiker':[gebr]})
                html_table = html_writer.htmlWriter().create_html_table(df)
                html_writer.htmlWriter().create_html_page(html_table, df, user.voornaam)
        elif option == 3:
                stat = input('Geef je station: ')
                mijn_station = mijn_app.stations.zoek_op_id(stat)
                df = pd.DataFrame({'slots':mijn_station.check_slot()})
                html_table = html_writer.htmlWriter().create_html_table(df)
                html_writer.htmlWriter().create_html_page(html_table, df, mijn_station.id)

    elif option == 9:
        for i in range(0,10):
            mijn_app.stations.simulatie(mijn_app.gebruikers_data, mijn_app.fietstransporteurs_data)

    elif option == 10:
        mijn_app.gebruikers_list.save_gebruikers()
        mijn_app.fietstransporteurs_list.save_fietstransporteurs()
        mijn_app.stations.save_stations()

    elif option == 11:
        print("Exit code....")
        exit()
    else:
        print('invalid option:', option, 'Try again...')


if __name__ == "__main__":
    main()
