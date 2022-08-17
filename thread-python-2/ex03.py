import os
import threading
import time


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

class ExecutaThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Isso é uma thread")
        time.sleep(3)
        clearConsole()


thread_simples = ExecutaThread()
thread_simples.start()
thread_simples.join()

