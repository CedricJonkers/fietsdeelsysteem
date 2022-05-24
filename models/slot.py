class Slot():
    def __init__(self,station, nummer, bezet):
        self.station = station
        self.nummer = nummer
        self.bezet = bezet

    def __repr__(self):
        if(self.bezet == True):
            return f"Slot {self.nummer} bezit een fiets"
        else:
            return f"Slot {self.nummer} bezit geen fiets"
        