
from threading import *

class Consumer(Thread):

    def __init__(self, co):
        Thread.__init__(self)
        self.co = co

    def run(self):
        with self.co:
            self.co.wait()
        print(f"{self.name} done")


class Producer(Thread):
    def __init__(self, co):
        Thread.__init__(self)
        self.co = co

    def run(self):
        with self.co:
            self.co.notifyAll()
        print(f"{self.name} done")

co = Condition()
c1 = Consumer(co)
c2 = Consumer(co)

p = Producer(co)

c1.start()
c2.start()

p.start()


