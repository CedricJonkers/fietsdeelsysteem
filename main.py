import models.gebruiker as gebruiker
import models.fiets as fiets
import models.station as station
import pandas as pd
import to_html


class App():
    def __init__(self):
        self.gebruikers_list = gebruiker.Gebruikers()
        self.station = station.Station(0, 0)
        self.stations = station.Stations()
        self.station_data = self.stations.read_stations()
        self.gebruikers_data = self.gebruikers_list.generate_gebruikers()


mijn_app = App()
# list_g = mijn_app.gebruikers_list.toon_gebruikers()
# list_s = mijn_app.stations.toon_stations()
# mijn_app.stations.add_slots_bikes()
# mijn_app.stations.check_slots(mijn_app.stations.add_slots_bikes())

option_menu = {
    1: 'Toon gebruikers',
    2: 'Toon stations',
    3: 'check slots',
    4: 'voeg fiets toe',
    5: 'exit'
}


def print_options():

    for key in option_menu.keys():
        print(key, '---', option_menu[key])


while(True):

    print_options()

    option = ""

    try:
        option = int(input('Enter option:'))

    except:

        print('option', option)

    if option == 1:
        list_g = mijn_app.gebruikers_list.toon_gebruikers()

    elif option == 2:
        list_s = mijn_app.stations.toon_stations()

    elif option == 3:
        mijn_app.stations.check_slots(mijn_app.stations.add_slots_bikes())

    elif option == 4:
        gebr = input('Geef je naam: ')
        mijn_app.gebruikers_list.zoek_op_naam(gebr)
        stat = input('Geef je station: ')
        mijn_station = mijn_app.stations.zoek_op_naam(stat)
        mijn_station.voeg_één_fiets_toe(gebr)

    elif option == 5:
        print("Exit code....")
        exit()
    else:
        print('invalid option:', option, 'Try again...')


# df = pd.DataFrame({'stations':mijn_app.stations.add_slots_bikes()})
# html_table = to_html.create_html_table(df)
# html_file = '''

# <!DOCTYPE html>
# <html>
# <head>
# <style>
# table {
#   border-collapse: collapse;
#   width: 30%;
# }

# th, td {
#   padding: 6px;
#   font-family: Helvetica, Arial, Helvetica;
#   font-size: 12px;
# }


# .header {
#   color: white;
#   background-color: black;
#   border-bottom:1pt solid black;
# }

# .text_column {
#   text-align: left;
# }

# .number_column {
#   text-align: right;
# }

# .even_row {
#   background-color: #f2f2f2;
# }

# </style>
# </head>

# <body>
#   <h1>A velo</h1>

# <div style="overflow-x:auto;">

# <table>
#   <thead>
#     <tr class = "header">
#       <th class = "text_column">'''+df.columns[0]+'''</th>
#     </tr>
#   </thead>
#   <tbody>
# ''' +html_table+ '''
#   </tbody>
#   </table>

# </div>

# </div>
# </body>
# </html>

# '''
# with open('df_from_loop.html', 'a') as f:
#     f.write(html_file)
# user = input("Wat is uw naam: ")
# mijn_app.gebruikers_list.zoek_op_naam(user)
# mijn_app.station.voeg_één_fiets_toe(mijn_app.gebruikers_list.zoek_op_naam(user))

# if __name__ == "__main__":
#     main()
