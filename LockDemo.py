
from threading import *
import time
import random

class Counter(Thread):
    def __init__(self, start = 0):
        Thread.__init__(self)
        self.lock = Lock()
        self.value =start

    def increment(self):
        print("lock is acquiring")
        with self.lock:
            self.value +=1
            print("lock is released")

    def run(self):
        for i in range(2):
            r = random.random()
            time.sleep(r)
            self.increment()
        print("job done")

c = Counter()
c.start()
c.join()