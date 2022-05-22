import models.fiets as fiets
import models.slot as slot
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

    def voeg_fiets_toe(self, slot):
        locatie = f"{self.straatnaam}, {self.postcode}, {self.district} in station: {slot}" 
        self.fietsen.append(fiets.Fiets("fietstransporteur", "in gebruik"))
        #logger.Logger().log_to_file(str("fietstransporteur heeft de fiets succesvol toegevoegd op locatie: " + str(locatie)))

    def voeg_één_fiets_toe(self, gebruiker, slot):
        self.fietsen.append(fiets.Fiets(gebruiker, "in gebruik"))
        locatie = f"{self.straatnaam}, {self.postcode}, {self.district} op slot nr {slot}"
        logger.Logger().log_to_file(str(gebruiker +" heeft de fiets succesvol toegevoegd op locatie: " + str(locatie)))
        for s in self.fietsen:
            print(len(self.fietsen))

    def voeg_slot_toe(self, nummer, bezet):
        self.slots.append(slot.Slot(self.id, nummer, bezet))
        return self.slots
    
    def check_slot(self):
        list = self.slots
        count = 0
        for key in list:
            slot = list[count]
            count+=1
        return list
    
    def geef_fiets(self):
        list = self.slots
        count = 0
        for key in list:
            slo = list[count]
            if(slo.bezet == True):
                list.pop(count)
                list.insert(count, slot.Slot(self.id, count, False))
                return slo
            count+=1

    def __str__(self):
        return f"{self.id}  : locatie: {self.straatnaam}, {self.postcode} {self.district} , aantal slots: {self.aantal_slots} + {self.slots}"


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

    def add_slots_bikes(self):
        for s in self.stations:
            print(s)
            for i in range(s.aantal_slots):
                x = random.randint(0, 1)
                if (x == 1):
                    s.voeg_slot_toe(i, True)
                else:
                    s.voeg_slot_toe(i, False)

    def zoek_op_id(self, naam):
        list = self.stations
        count = 0
        for key in list:
            stat = list[count]
            statnaam = stat.id
            if (statnaam == int(naam)):
                return stat
            count += 1

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
