# extending the Thread class
from time import sleep, ctime
from threading import Thread
class CustomThread(Thread):
    def run(self):
        sleep(1)
        print(f'{ctime()}This is coming from another thread')
        
thread = CustomThread()
thread.start()
print(f'{ctime()}Waitting for the thread to finish')
thread.join()