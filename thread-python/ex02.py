import os
import threading
import time

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def show_fruit(name):
    print(f"{name}")
    time.sleep(3)
    clearConsole()


class ShowFruits(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        show_fruit(self.name)


fruit1 = ShowFruits("Banana")
fruit2 = ShowFruits("Maça")
fruit3 = ShowFruits("Pera")
fruit4 = ShowFruits("Abacaxi")
fruit5 = ShowFruits("Maracuja")

fruit1.start()
fruit1.join()

fruit2.start()
fruit2.join()

fruit3.start()
fruit3.join()

fruit4.start()
fruit4.join()

fruit5.start()
fruit5.join()

