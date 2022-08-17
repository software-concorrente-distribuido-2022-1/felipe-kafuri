import threading

class ExecutaThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Isso é uma thread")


thread_simples = ExecutaThread()
thread_simples.start()
thread_simples.join()

