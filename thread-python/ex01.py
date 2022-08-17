import threading


def count_to_hundred():
    for i in range(1, 101):
        print(i)

class HundredCounter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        count_to_hundred()
        print("\nPrograma finalizado")


t = HundredCounter()
t.start()
t.join()


