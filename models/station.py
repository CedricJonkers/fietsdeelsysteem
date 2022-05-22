import models.fiets as fiets
import models.slot as slot
import logger as logger
import random


class Station():
    def __init__(self, id, slots):
        self.id = id
        self.slots = slots
        self.fietsen = []

    def voeg_fiets_toe(self, *fietsen):
        for een_fiets in fietsen:
            self.fietsen.append(fiets.Fiets("fietstransporteur", "in gebruik"))
            for s in self.fietsen:
                logger.Logger().log_to_file(str("toegevoegd door: " + s.gebruiker))
                print("toegevoegd door: " + s.gebruiker)

    def voeg_één_fiets_toe(self, gebruiker):
        self.fietsen.append(fiets.Fiets(gebruiker, "in gebruik"))
        for s in self.fietsen:
            logger.Logger().log_to_file(str(s.gebruiker + " heeft de fiets succesvol ontgrendeld!"))
            # print(str(s.gebruiker) + "heeft de fiets succesvol ontgrendeld!")
            print(len(self.fietsen))

    def doe_fiets_weg(self, gebruiker, *fietsen):
        for een_fiets in fietsen:
            if len(self.fietsen) != 0:
                self.fietsen.remove(fiets.Fiets(gebruiker, "in gebruik"))
            for s in self.fietsen:
                print(s)

    def __str__(self):
        return f"{self.id}  : {self.id} , {self.slots}"


class Stations():
    def __init__(self):
        self.stations = []
        self.slots = []

    def read_stations(self):
        with open(r"dataset\velo_data.txt", "r") as station_bestand:
            aantal_slots = 0
            id = ""
            station = ""
            for station in station_bestand:
                station = station.rstrip().split(",")
                id = station[11]
                if station[13].isnumeric():
                    aantal_slots = int(station[13])
                    station = Station(id, aantal_slots)
                    self.stations.append(station)
            return self.stations

    def add_slots_bikes(self):
        for s in self.stations:
            print(s)
            for i in range(s.slots):
                x = random.randint(0, 1)
                if (x == 1):
                    één_slot = slot.Slot(s.id, i, True)
                    Station(s.id, s.slots).voeg_fiets_toe(x)
                else:
                    één_slot = slot.Slot(s.id, i, False)
                self.slots.append(één_slot)
                print(één_slot)
        return self.slots   

    def zoek_op_naam(self, naam):
        list = self.stations
        count = 0
        for key in list:
            stat = list[count]
            statnaam = stat.id
            if (statnaam == naam):
                print("Gevonde")
                return stat
            count+=1

    def check_slots(self, *slots):
        for stat in self.stations:
            print(stat.slots)



    def toon_stations(self):
        list = self.stations
        count = 0
        for key in list:
            sta = list[count]
            print(sta)
            count+=1
        return list

    def __repr__(self):
        return '\n'.join(str(stat) for stat in self.stations)
