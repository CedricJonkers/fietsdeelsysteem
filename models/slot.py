class Slot():
    def __init__(self,station, nummer, bezet, fiets_id):
        self.station = station
        self.nummer = nummer
        self.bezet = bezet
        self.fiets_id = fiets_id

    def __repr__(self):
        if(self.bezet == True):
            return f"Slot {self.nummer} bezit fiets met id {self.fiets_id}"
        else:
            return f"Slot {self.nummer} bezit geen fiets"
        