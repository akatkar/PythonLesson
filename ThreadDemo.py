from threading import *
from time import sleep

class MyThread(Thread):

    def __init__(self, name, delay=0.5):
        Thread.__init__(self, name=name)
        self.delay = delay

    def run(self):
        i = 0
        while i<5:
            sleep(self.delay)
            i +=1
        print(f"{self.name} finished")


th = [MyThread("M1"), MyThread("M2",0.4)]

for t in th:
    t.start()

print("check point 1")
for t in th:
    t.join()
print("check point 2")
