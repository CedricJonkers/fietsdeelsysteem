from pip import main
import models.fietstransporteur as fietstransporteur
import models.gebruiker as gebruiker
import models.fiets as fiets
import models.station as station
import sys, os
import pandas as pd
import html_writer as html_writer
import sys
import logger


class App():
    def __init__(self):
        self.gebruikers_list = gebruiker.Gebruikers()
        self.fietstransporteurs_list = fietstransporteur.Fietstransporteurs()
        self.station = station.Station(0, "Baron Sadoinestraat (2660)","",0,0,0)
        self.stations = station.Stations()
        self.station_data = self.stations.read_stations()
        data = input("Wilt u de vorige configuratie gebruiken?(y/n)")
        if (data == "y"):
            self.gebruikers_data = self.gebruikers_list.read_gebruikers()
            self.fietstransporteurs_data = self.fietstransporteurs_list.read_fietstransporteurs()
            self.stations.initialise_stations(self.gebruikers_list)
        else:
            aantal_gebruikers = int(input('Hoeveel gebruikers wilt u? '))
            self.gebruikers_data = self.gebruikers_list.generate_gebruikers(aantal_gebruikers)
            aantal_fietstransporteurs = int(input('Hoeveel fietstransporteurs wilt u? '))
            self.fietstransporteurs_data = self.fietstransporteurs_list.generate_fietstransporteurs(aantal_fietstransporteurs)
            self.stations.add_slots_bikes(self.fietstransporteurs_data)


mijn_app = App()

if len(sys.argv) == 2 and sys.argv[1] == "sim":
    mijn_app.stations.simulatie(mijn_app.gebruikers_data, mijn_app.fietstransporteurs_data)
    opnieuw = input("Wilt u de simulatie nog eens runnen?(Y/N)")
    while opnieuw != "N":
        opnieuw = input("Wilt u de simulatie nog eens runnen?(Y/N)")
        mijn_app.stations.simulatie(mijn_app.gebruikers_data, mijn_app.fietstransporteurs_data)
    if (opnieuw == "N"):
        mijn_app.gebruikers_list.save_gebruikers()
        mijn_app.fietstransporteurs_list.save_fietstransporteurs()
        mijn_app.stations.save_stations()
        print("\nExit code....")
        exit()
            



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
    10: 'save and exit '
}

sub_option_menu = {
    1: 'Fiets',
    2: 'Gebruiker',
    3: 'Station'
}


def print_options(y, tekst):
    size = os.get_terminal_size()
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
          #id = mijn_app.stations.check_fiets_gebr(user)
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
        print_options(sub_option_menu,"Van welk onderdeel wil je een beeld krijgen: ")
        option = ""
        try:
            option = int(input('\nEnter option: '))
        except:
            print("option", option, "\n")
        if option == 1:
            fie_id = int(input('Geef je fietsid: '))
            obj = [mijn_app.stations.check_fiets(fie_id)]
            bestand_naam = obj[0].id
            tabel_naam = "fiets " + str(bestand_naam)
            log_zoek = bestand_naam
        elif option == 2:
            gebr = input('Geef je naam: ')
            user = mijn_app.gebruikers_list.zoek_op_naam(gebr)
            fie_id = mijn_app.stations.zoek_fiets_gebruiker(user)
            obj = [mijn_app.stations.check_fiets(fie_id)]
            try:
                bestand_naam = user.voornaam
                tabel_naam = "gebruiker: " + bestand_naam +" "+ user.achternaam
                log_zoek = user.achternaam + " " +bestand_naam
            except:
                print("Deze gebruiker bestaat niet")
                break
        elif option == 3:
            stat = input('Geef je station id: ')
            cur_station = mijn_app.stations.zoek_op_id(stat)
            cur_fietsen = cur_station.check_fiets_station()
            obj = cur_station.check_slot()
            tabel_naam = f"{cur_station.id}  : locatie: {cur_station.straatnaam}, {cur_station.postcode} {cur_station.district}"
            bestand_naam = cur_station.id
            fietsen_naam = str("fietsen" + str(cur_station.id))
            log_zoek = str(cur_station.id)
            df_fietsen = pd.DataFrame({"fietsen":cur_fietsen})
            html_table_fietsen = html_writer.htmlWriter().create_html_table(df_fietsen)
            html_writer.htmlWriter().create_html_page(html_table_fietsen, df_fietsen, fietsen_naam,bestand_naam, "Home")
        
        try:
            log_button = "log"
            try:
                log_button = "log" + str(bestand_naam)
                logs = logger.Logger().read_by_name(str(log_zoek))
                df_log = pd.DataFrame({'log':logs})
                html_table_log = html_writer.htmlWriter().create_html_table(df_log)
                if (option == 3):
                    html_writer.htmlWriter().create_html_page(html_table_log, df_log,log_button, fietsen_naam,"Fietsen log")
                else:
                    html_writer.htmlWriter().create_html_page(html_table_log, df_log,log_button, bestand_naam,"Back")
            except:
                print("geen logs")
            df = pd.DataFrame({tabel_naam:obj})
            html_table = html_writer.htmlWriter().create_html_table(df)
            html_writer.htmlWriter().create_html_page(html_table, df, bestand_naam,log_button,"See logs")
            os.system(f"start _site/{bestand_naam}.html")
        except:
            print("Er is iets fout gelopen")

    elif option == 9:
        mijn_app.stations.simulatie(mijn_app.gebruikers_data, mijn_app.fietstransporteurs_data)

    elif option == 10:
        mijn_app.gebruikers_list.save_gebruikers()
        mijn_app.fietstransporteurs_list.save_fietstransporteurs()
        mijn_app.stations.save_stations()
        print("\nExit code....")
        exit()
    else:
        print('invalid option:', option, 'Try again...')
    
    # if __name__ == "__main__":
    #     main()
