import models.fiets as fiets
import models.slot as slot
import models.fietstransporteur as fietstransporteur
import logger as logger
import models.gebruiker as gebruiker
import random
import json


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

    def voeg_slot_toe(self, nummer, bezet):
        self.slots.append(slot.Slot(self.id, nummer, bezet))
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
                list_slots.pop(count)
                list_slots.insert(count, slot.Slot(self.id, count, False))
                for f in list_fietsen:
                    fie = list_fietsen[count]
                    list_fietsen.pop(count)
                    list_fietsen.insert(count, fiets.Fiets(gebr, True, fie.id))
                return slo
            count += 1

    def voeg_plaats_toe(self, nummer):
        list_slots = self.slots
        count_slot = 0
        for key in list_slots:
            slo = list_slots[count_slot]
            if(slo.nummer == int(nummer)):
                if(slo.bezet == False):
                    list_slots.pop(count_slot)
                    list_slots.insert(count_slot, slot.Slot(
                        self.id, count_slot, True))
                    return slo
                else:
                    print("Dit slot bevat al een fiets")
                    return "Dit slot bevat al een fiets"
            count_slot += 1

    def __str__(self):
        return f"{self.id}  : locatie: {self.straatnaam}, {self.postcode} {self.district} , aantal slots: {self.aantal_slots}, aantal fietsen: {len(self.fietsen)}\n {self.slots}\n"


class Stations():
    def __init__(self):
        self.stations = []

    def read_stations(self):
        fileObject = open(r"dataset\velo_data.json", "r")
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
        return self.stations

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
                    s.voeg_slot_toe(i, True)
                    s.voeg_fiets_toe(
                        i, count, transporteurslist[transporteurcount])
                    count += 1
                else:
                    s.voeg_slot_toe(i, False)
    
    def zet_fietsen_in_wagen(self, stat_teveel, fietstransporteur):
        return_list = []
        count = 0
        if (stat_teveel != None):
            aantal_fietsen = round(len(stat_teveel.fietsen)/2)
            for i in stat_teveel.fietsen:
                if(count < aantal_fietsen):
                    print(i.gebruiker)
                    return_list.append(fiets.Fiets(fietstransporteur, True, i.id))
                    stat_teveel.fietsen.remove(i)
                    count+=1
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
    
    def verwijder_fiets(self, gebr):
        list_station = self.stations
        count_stat = 0
        for key in list_station:
            if (count_stat < len(list_station)):
                stat = list_station[count_stat]
            for f in stat.fietsen:
                if (f.gebruiker == gebr):
                    print("je hebt de fiets succesvol terug gebracht")
                    stat.fietsen.remove(f)
                    stat.fietsen.append(fiets.Fiets(gebr, False, f.id))
                    return gebr
            count_stat+=1

    def check_fiets(self, id):
        list_station = self.stations
        count_stat = 0
        for key in list_station:
            if (count_stat < len(list_station)):
                stat = list_station[count_stat]
            for f in stat.fietsen:
                if (f.id == id):
                    return f
            count_stat+=1

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

    def __repr__(self):
        return '\n'.join(str(stat) for stat in self.stations)
