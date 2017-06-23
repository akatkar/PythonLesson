
from threading import *

class Racer(Thread):

    def __init__(self, name, start_signal):
        Thread.__init__(self)
        self.name = name
        self.start_signal = start_signal

    def run(self):
        self.start_signal.wait()
        print(f"{self.name} finished")

class Race:
    def __init__(self, racer_list):
        self.start_signal = Event()
        racers = [Racer(racer,self.start_signal) for racer in racer_list]
        for t in racers:
            t.start()
    def race_start(self):
        print("signal set")
        self.start_signal.set()

r = Race(["rabbit","turtle","lion","tiger"])
r.race_start()