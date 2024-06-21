# running a function in another thread
from time import sleep, ctime
from threading import Thread
def task():
    sleep(1)
    print(f'{ctime()}This os from another thread')

thread = Thread(target=task)
thread.start()
print(f'{ctime()}Waitting for the thread')
thread.join()