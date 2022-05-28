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

    def voeg_fiets_toe(self, slot, id, gebr):
        locatie = f"{self.straatnaam}, {self.postcode}, {self.district} in station met id: {self.id} op slotnr: {slot}"
        self.fietsen.append(fiets.Fiets(gebr, False, id))
        #logger.Logger().log_to_file(str(gebr.achternaam + " " +  gebr.voornaam + " heeft een fiets geplaatst bij de "+ str(locatie)))
        return self.fietsen

    def voeg_één_fiets_toe(self, gebruiker, slot, id):
        self.fietsen.append(fiets.Fiets(gebruiker, False, id))
        locatie = f"{self.straatnaam}, {self.postcode}, {self.district} op slot nr {slot}"
        logger.Logger().log_to_file(str(gebruiker + " heeft de fiets met id: " +
                                        {id} + " succesvol toegevoegd op locatie: " + str(locatie)))
        for s in self.fietsen:
            print(len(self.fietsen))

    def voeg_slot_toe(self, nummer, bezet, fiets_id):
        self.slots.append(slot.Slot(self.id, nummer, bezet, fiets_id))
        return self.slots

    def check_fiets(self):
        list = self.fietsen
        count = 0
        for key in list:
            slot = list[count]
            count += 1
        return list

    def check_slot(self):
        list = self.slots
        count = 0
        for key in list:
            slot = list[count]
            count += 1
        return list

    def geef_fiets(self, gebr):
        list_slots = self.slots
        list_fietsen = self.fietsen
        count = 0
        for key in list_slots:
            slo = list_slots[count]
            if(slo.bezet == True):
                list_slots.remove(slo)
                list_slots.insert(count, slot.Slot(self.id, count, False, None))
                fie = list_fietsen[count]
                list_fietsen.remove(self.fiets_op_id(slo.fiets_id))
                list_fietsen.append(fiets.Fiets(gebr, True, slo.fiets_id))
                print(gebr)
                print(slo)
                return slo
            count += 1
    
    def fiets_op_id(self, fiets_id):
        for i in self.fietsen:
            print(i.id)
            if (i.id == fiets_id):
                print("ok")
                print(i)
                return i

    def voeg_plaats_toe(self, nummer, fiets_id):
        list_slots = self.slots
        count_slot = 0
        for key in list_slots:
            slo = list_slots[count_slot]
            if(slo.nummer == int(nummer)):
                if(slo.bezet == False):
                    list_slots.remove(slo)
                    list_slots.insert(count_slot, slot.Slot(
                        self.id, count_slot, True, fiets_id))
                    return slo
                else:
                    print("Dit slot bevat al een fiets")
                    return "Dit slot bevat al een fiets"
            count_slot += 1
    
    #slots to stations json
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
            print(station)
        return self.stations

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

    def add_slots_bikes(self, transporteurslist):
        count = 0
        transporteurcount = 0
        for s in self.stations:
            print(s)
            transporteurcount += 1
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
            for i in stat_teveel.fietsen:
                if(count < aantal_fietsen):
                    print(i.gebruiker)
                    return_list.append(fiets.Fiets(
                        fietstransporteur, True, i.id))
                    stat_teveel.fietsen.remove(i)
                    count += 1
        print(return_list)
        return return_list

    def zet_fietsen_in_nieuw_station(self, fietsen, stat_teweinig):
        if(stat_teweinig != None):
            if (fietsen != None):
                for f in fietsen:
                    stat_teweinig.fietsen.append(f)
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

    def verwijder_fiets(self, gebr, station):
        list_station = self.stations
        count_stat = 0
        for key in list_station:
            if (count_stat < len(list_station)):
                stat = list_station[count_stat]
            for f in stat.fietsen:
                if (f.gebruiker == gebr):
                    print("_Q_Q_Q")
                    print(f)
                    stat.fietsen.remove(f)
                    print(stat.fietsen)
                    station.fietsen.append(fiets.Fiets(gebr, False, f.id))
                    print("_Q_Q_Q")
                    print(stat.fietsen)
                    return f"{f.gebruiker} heeft de fiets met id {f.id} succesvol terug gebracht op station met id {stat.id}"
            count_stat += 1

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

    def check_fiets_gebr(self, naam):
        list_station = self.stations
        count_stat = 0
        for key in list_station:
            if (count_stat < len(list_station)):
                stat = list_station[count_stat]
            for f in stat.fietsen:
                if (f.gebruiker == naam):
                    return f.id
            count_stat += 1

    def zoek_op_postcode(self, postcode):
        list = self.stations
        returnlist = []
        count = 0
        for key in list:
            stat = list[count]
            statpostcode = stat.postcode
            if (statpostcode == postcode):
                returnlist.append(stat.straatnaam)
            count += 1
        return returnlist

    def check_slots(self):
        for stat in self.stations:
            print("station met id: " + stat.id)
            list = stat.check_slot()
        return list

    def toon_stations(self):
        list = self.stations
        count = 0
        for key in list:
            sta = list[count]
            print(sta)
            count += 1
        return list

    def simulatie(self, gebruikers, fietstransporteurs):
        # gebruiker neemt een fiets
        gebruiker = self.geef_gebruiker(gebruikers)
        station_begin = self.geef_station()
        station_begin.geef_fiets(gebruiker)

        # gebruiker zet de fiets terug
        station_eind = self.geef_station()
        for s in station_eind.slots:
            if (s.bezet == False):
                station_eind.voeg_plaats_toe(s.nummer, self.check_fiets_gebr(gebruiker))
                self.verwijder_fiets(gebruiker, station_eind)
                return
            # else:
            #     print("pech, opnieuw")
    
    # geeft een random gebruiker uit de json voor de simulatie
    def geef_gebruiker(self, gebruikers):
        for x in gebruikers:
            if x.tijd_bezig == 0:
                y = random.randint(0,5)
                if (y == 1):
                    print(x)
                    return x

    # geeft een random station uit de json voor de simulatie
    def geef_station(self):
        for x in self.stations:
            y = random.randint(0,5)
            if (y == 1):
                print(x)
                return x



    def __repr__(self):
        return '\n'.join(str(stat) for stat in self.stations)
