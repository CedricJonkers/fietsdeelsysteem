import time


class Tijd():
    def __init__(self):
        self
    
    def start_tijd():
        start_time = time.time()
        return start_time

    def stop_tijd():
        end_time = time.time()
        return end_time
    
    def tijd_op_fiets(start_tijd, stop_tijd):
        tijd_verschil = stop_tijd - start_tijd
        return round(tijd_verschil*100)
        

    def __repr__(self):
        return f"{self.tijd_per_rit}"