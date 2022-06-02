import time
import sys
import datetime

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

    def tijd_show():
        for i in range(10,0,-1):
            sys.stdout.write(str(i)+' ')
            sys.stdout.flush()
            time.sleep(1)
    
    def wacht_tijd(duur):
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(animation)*duur):
            time.sleep(1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")
        return len(animation)*duur