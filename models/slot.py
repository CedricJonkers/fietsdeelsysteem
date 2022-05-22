class Slot():
    def __init__(self,station, nummer, bezet):
        self.station = station
        self.nummer = nummer
        self.bezet = bezet
    
    def check_bezet(self):
        if (self.bezet == True):
            return "bezet"
        else:
            return "vrij"

    def __repr__(self):
        if(self.bezet == True):
            return f"{self.nummer} bezit een fiets"
        else:
            return f"{self.nummer} bezit geen fiets"
        