import os
from re import X
import models.fiets as fiets
import models.slot as slot
import models.fietstransporteur as fietstransporteur
import logger as logger
import models.gebruiker as gebruiker
import random
import json

from models.tijd import Tijd


class Station():
    def __init__(self, id, straatnaam, district, postcode, objectcode, aantal_slots):
        straatnaam = str(straatnaam).split(' (', 1)
        self.id = id
        self.straatnaam = straatnaam[0]
        self.postcode = postcode
        self.district = district
        self.objectcode = objectcode
        self.aantal_slots = aantal_slots
        self.fietsen = []
        self.slots = []
    
    # voegt fiets aan de fietsenlijst toe
    def voeg_fiets_toe(self, slot, id, gebr):
        locatie = f"{self.straatnaam}, {self.postcode}, {self.district} in station met id: {self.id} op slotnr: {slot}"
        self.fietsen.append(fiets.Fiets(gebr, False, id))
        #logger.Logger().log_to_file(str(gebr.achternaam + " " +  gebr.voornaam + " heeft een fiets geplaatst bij de "+ str(locatie)))
        return self.fietsen

    # voegt een slot toe aan het station
    def voeg_slot_toe(self, nummer, bezet, fiets_id):
        self.slots.append(slot.Slot(self.id, nummer, bezet, fiets_id))
        return self.slots
    
    # checkt het aantal volle slots
    def check_slot_met_fiets(self):
        aantal_slots = 0
        for s in self.slots:
            if (s.bezet == True):
                aantal_slots+=1
        return aantal_slots
    
    # checkt naar een leeg slot
    def check_leeg_slot(self):
        slot = -1
        for s in self.slots:
            if (s.bezet == False):
                slot = s
                return slot
    
    # checht de fietsen van het station
    def check_fiets_station(self):
        list = self.fietsen
        count = 0
        for key in list:
            slot = list[count]
            count += 1
        return list
    
    # laat de slots van het station zien
    def check_slot(self):
        list = self.slots
        count = 0
        for key in list:
            slot = list[count]
            count += 1
        return list

    # geeft een slotnummer aan de gebruiker, zet haalt de fiets uit het slot
    def geef_fiets(self, gebr, stations):
        list_slots = self.slots
        list_fietsen = self.fietsen
        count = 0
        for key in list_slots:
            slo = list_slots[count]
            if(slo.bezet == True):
                list_slots.remove(slo)
                list_slots.insert(count, slot.Slot(
                    self.id, count, False, None))
                x = stations.check_fiets(slo.fiets_id)
                if (x in list_fietsen):
                    list_fietsen.remove(x)
                    list_fietsen.append(fiets.Fiets(gebr, True, slo.fiets_id))
                else:
                    stations.remove_fiets(slo.fiets_id)
                    list_fietsen.append(fiets.Fiets(gebr, True, slo.fiets_id))
                return slo
            count += 1
    
    # een gebruiker zet de fiets terug 
    def voeg_plaats_toe(self, slot_gegeven, fiets_id):
        list_slots = self.slots
        count_slot = 0
        for key in list_slots:
            slo = list_slots[count_slot]
            if(slo == slot_gegeven and slo.bezet == False):
                list_slots.remove(slo)
                list_slots.insert(count_slot, slot.Slot(self.id, count_slot, True, fiets_id))
                return slo
            count_slot += 1

    # slots to stations json
    def save_slots(self):
        data = []
        for s in self.slots:
            data.append({
                'slot': {
                    'id': s.nummer,
                    'bezet': s.bezet,
                    'fiets': s.fiets_id
                }
            })
        print(data)
        return data

    def __str__(self):
        return f"{self.id}  : locatie: {self.straatnaam}, {self.postcode} {self.district} , aantal slots: {self.aantal_slots}, aantal fietsen: {len(self.fietsen)}\n {self.slots}\n"


class Stations():
    def __init__(self):
        self.stations = []
    
    # leest de stations uit de json
    def read_stations(self):
        fileObject = open(r"dataset_default\velo_data.json", "r")
        jsonContent = fileObject.read()
        station_bestand = json.loads(jsonContent)
        id = ""
        straatnaam = ""
        district = ""
        postcode = ""
        objectcode = ""
        aantal_slots = 0
        station = ""
        for station in station_bestand:
            id = station['properties']['OBJECTID']
            straatnaam = station['properties']['Straatnaam']
            district = station['properties']['District']
            postcode = station['properties']['Postcode']
            objectcode = station['properties']['Objectcode']
            aantal_slots = int(station['properties']['Aantal_plaatsen'])
            station = Station(id, straatnaam, district, postcode,
                              objectcode, aantal_slots)
            self.stations.append(station)
            print(f"reading stations...")
            os.system('cls')
        return self.stations
    
    # slaagt de stations op
    def save_stations(self):
        data = []
        list = self.stations
        count = 0
        try:
            for key in list:
                stat = list[count]
                data.append({
                    'properties': {
                        'OBJECTID': stat.id,
                        'Straatnaam': stat.straatnaam,
                        'District': stat.district,
                        'Postcode': stat.postcode,
                        'Objectcode': stat.objectcode,
                        'Aantal_plaatsen': stat.aantal_slots,
                    },
                    'slots': [stat.save_slots()]
                })
                count += 1
            with open("dataset_save\stations.json", 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except:
            print(
                "Er heeft zich een probleem voorgedaan bij het wegschrijven naar het uitvoerbestand")

    # voegt bij het begin van de simulatie de fietsen en slots aan de stations
    def add_slots_bikes(self, transporteurslist):
        count = 0
        transporteurcount = 0
        for s in self.stations:
            transporteurcount += 1
            print(f"fietsen toevoegen aan station: {s}")
            os.system('cls')
            if (transporteurcount >= len(transporteurslist)):
                transporteurcount = 0
            for i in range(s.aantal_slots):
                x = random.randint(0, 1)
                if (x == 1):
                    start_tijd = Tijd.start_tijd()
                    # print(start_tijd)
                    s.voeg_slot_toe(i, True, count)
                    s.voeg_fiets_toe(
                        i, count, transporteurslist[transporteurcount])
                    count += 1
                    stop_tijd = Tijd.stop_tijd()
                    transporteurslist[transporteurcount].tijd_bezig = Tijd.tijd_op_fiets(
                        start_tijd, stop_tijd)
                    #print(Tijd.tijd_op_fiets(start_tijd, stop_tijd))
                else:
                    s.voeg_slot_toe(i, False, None)

    def zet_fietsen_in_wagen(self, stat_teveel, fietstransporteur):
        return_list = []
        count = 0
        if (stat_teveel != None):
            aantal_fietsen = round(len(stat_teveel.fietsen)/2)
            for s in stat_teveel.slots:
                if (s.bezet == False):
                    if(count < aantal_fietsen):
                        print(stat_teveel)
                        f = stat_teveel.geef_fiets(fietstransporteur, self)
                        return_list.append(f)
            # for i in stat_teveel.fietsen:
            #     if(count < aantal_fietsen):
            #         print(i.gebruiker)
            #         return_list.append(fiets.Fiets(
            #             fietstransporteur, True, i.id))
            #         stat_teveel.fietsen.remove(i)
                    # stat_teveel.voeg_plaats_toe()
                    count += 1
        return return_list

    def zet_fietsen_in_nieuw_station(self, fietsen, stat_teweinig, fietstransporteur):
        if(stat_teweinig != None):
            if (fietsen != None):
                # for f in fietsen:
                #     stat_teweinig.fietsen.append(fiets.Fiets(f.gebruiker, False, f.id))
                for s in stat_teweinig.slots:
                    if (s.bezet == False):
                        stat_teweinig.voeg_plaats_toe(
                            s.nummer, self.check_fiets_gebr(fietstransporteur))
                        self.verwijder_fiets(fietstransporteur, stat_teweinig)
            return stat_teweinig.fietsen

    def check_teveel_fietsen(self):
        list = self.stations
        count = 0
        for key in list:
            stat = list[count]
            d = len(stat.slots) - len(stat.fietsen)
            if (d <= round(len(stat.slots)/4)):
                return stat
            count += 1

    def check_teweinig_fietsen(self):
        list = self.stations
        count = 0
        for key in list:
            stat = list[count]
            d = len(stat.slots) - len(stat.fietsen)
            if (d >= round(len(stat.slots)/4)):
                return stat
            count += 1
    
    # zoekt station op id
    def zoek_op_id(self, naam):
        list = self.stations
        count = 0
        for key in list:
            stat = list[count]
            statnaam = stat.id
            naam = int(naam)
            if (isinstance(naam, int) == True):
                if (statnaam == int(naam)):
                    return stat
            count += 1

    # zoekt de fiets van de gebruiker en haalt deze uit de lijst van de fietsen van het vorige station + voegt deze toe aan het nieuwe station
    def verwijder_fiets(self, gebr, station):
        list_station = self.stations
        count_stat = 0
        for key in list_station:
            if (count_stat < len(list_station)):
                stat = list_station[count_stat]
            for f in stat.fietsen:
                if (f.gebruiker == gebr and f.in_gebruik == True):
                    stat.fietsen.remove(f)
                    station.fietsen.append(fiets.Fiets(gebr, False, f.id))
                    if (gebr != None):
                        print('-------')
                        print(f"{f.gebruiker.achternaam} {f.gebruiker.voornaam} heeft de fiets met id {f.id} succesvol terug gebracht op station met id {stat.id}")
                        print('-------')
                        return f"{f.gebruiker} heeft de fiets met id {f.id} succesvol terug gebracht op station met id {stat.id}"
                elif (f.gebruiker == gebr and f.in_gebruik == False):
                    print(f"{f.gebruiker.achternaam} {f.gebruiker.voornaam} is aan het fietsen")
            count_stat += 1

    # kijkt of de fiets met {id} in gebruik is
    def check_fiets(self, id):
        list_station = self.stations
        count_stat = 0
        for key in list_station:
            if (count_stat < len(list_station)):
                stat = list_station[count_stat]
            for f in stat.fietsen:
                if (f.id == id):
                    return f
            count_stat += 1

    # zoekt de fiets_id van de gebruiker
    def zoek_fiets_gebruiker(self, naam):
        list_station = self.stations
        count_stat = 0
        for key in list_station:
            if (count_stat < len(list_station)):
                stat = list_station[count_stat]
            for f in stat.fietsen:
                if (f.gebruiker == naam and f.in_gebruik == True):
                    return f.id
            count_stat += 1

    # zet de fiets die de gebruiker juist heeft genomen op zijn naam
    def remove_fiets(self, fiets_id):
        list = self.stations
        count = 0
        for key in list:
            stat = list[count]
            for x in stat.fietsen:
                if (x.id == fiets_id):
                    stat.fietsen.remove(x)
                    return stat
            count += 1

    # toont alle stations
    def toon_stations(self):
        list = self.stations
        count = 0
        for key in list:
            sta = list[count]
            # print(sta)
            count += 1
        return list

    def simulatie(self, gebruikers, fietstransporteurs):
        if (len(gebruikers)<=5):
            print("Geef minstens 5 gebruikers")
            exit()
        for i in range(0,random.randint(1,5)):
            print(i)
            gebruiker = self.geef_gebruiker(gebruikers)
            station_begin = self.geef_station()
            id = station_begin.geef_fiets(gebruiker, self)
            if (gebruiker != None):
                logger.Logger().log_to_file(str(gebruiker.achternaam + " " + gebruiker.voornaam + " heeft een fiets gehaalt bij station " + str(station_begin.id) + " slot: " + str(id)))
        
        gebruikers_met_fiets = self.check_fietsen_met_gebruiker()
        index = random.randint(0,len(gebruikers_met_fiets)-1) 
        gebruiker_stop = gebruikers_met_fiets[index]
        station_eind = self.geef_station()
        if (station_eind.check_leeg_slot() != -1 and gebruiker_stop.gebruiker != None):
            station_eind.voeg_plaats_toe(station_eind.check_leeg_slot(), self.zoek_fiets_gebruiker(gebruiker_stop.gebruiker))
            print(f"fiets: {id}: van {station_begin.id} -> {station_eind.id} door {gebruiker_stop.gebruiker}")
            self.verwijder_fiets(gebruiker_stop.gebruiker, station_eind)
            logger.Logger().log_to_file(str(gebruiker_stop.gebruiker.achternaam + " " + gebruiker_stop.gebruiker.voornaam + " heeft een fiets teruggebracht bij station " + str(station_eind.id)))
            # y = self.check_fietsen_met_gebruiker()
            # print(y)
        else:
            print(gebruikers_met_fiets)
            print("station leeg, of elke gebruiker heeft een fiets")
            exit()
        # # if(len(station_begin.fietsen) < 5):
        # #     nieuw_station = self.check_teveel_fietsen()
        # #     fietstransporteur = self.geef_gebruiker(fietstransporteurs)
        # #     teveel_fietsen = self.zet_fietsen_in_wagen(nieuw_station, fietstransporteur)
        # #     self.zet_fietsen_in_nieuw_station(teveel_fietsen, station_begin, fietstransporteur)
        # #     print(fietstransporteur)
        # #     print(teveel_fietsen)
        # #     print(nieuw_station)
        # #     print(station_begin)
        # #     print("fietstr")
        # #     logger.Logger().log_to_file(fietstransporteur)
        # #     logger.Logger().log_to_file(nieuw_station)

    # geeft een random gebruiker uit de json voor de simulatie
    def geef_gebruiker(self, gebruikers):
        for i in range(0,len(gebruikers)):
            gebruiker = random.choice(gebruikers)
            if (self.check_fiets_gebruiker(gebruiker) == False):
                return gebruiker
            elif(i>len(gebruikers)):
                print("elke gebruiker bevat een fiets")
                return None
    
    # zoekt de gebruikers die geen fietsen hebben
    def check_fietsen_met_gebruiker(self):
        list = self.stations
        count = 0
        gebruikers_met_fiets = []
        for key in list:
            stat = list[count]
            for s in stat.fietsen:
                if (s.in_gebruik == True):
                    gebruikers_met_fiets.append(s)
                    if (s.gebruiker == None):
                        gebruikers_met_fiets.remove(s)
            count+=1
        return gebruikers_met_fiets

                
    
    # checkt of de gebruiker al een fiets heeft
    def check_fiets_gebruiker(self, gebruiker):
        list = self.stations
        bevat_fiets = False
        count = 0
        for key in list:
            stat = list[count]
            for s in stat.fietsen:
                if (s.in_gebruik == True):
                    if (s.gebruiker == gebruiker):
                        bevat_fiets = True
                        return bevat_fiets
                    else:
                        bevat_fiets = False
                else:
                    bevat_fiets = False
            count += 1
        return bevat_fiets

    # geeft een random station uit de json voor de simulatie, gebruikt de methode geef_station_id
    def geef_station(self):
        id_list = self.geef_station_id()
        niet_gevonden = True
        while niet_gevonden == True:
            station_id = random.choice(id_list)
            if (self.zoek_op_id(station_id) != None and self.zoek_op_id(station_id).check_slot_met_fiets() != 0):
                niet_gevonden = False
                return self.zoek_op_id(station_id)

    # geeft het id per station mee in een list
    def geef_station_id(self):
        list = self.stations
        stat_id = []
        count = 0
        for key in list:
            sta = list[count]
            stat_id.append(sta.id)
            count += 1
        return stat_id

    def __repr__(self):
        return '\n'.join(str(stat) for stat in self.stations)
