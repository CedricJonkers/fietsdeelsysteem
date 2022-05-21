class Slot():
    def __init__(self,station, nummer, bezet):
        self.station = station
        self.nummer = nummer
        self.bezet = bezet

    def __repr__(self):
        return f"Station: {self.station} slot nr: {self.nummer} bezit {self.bezet} fiets"
        