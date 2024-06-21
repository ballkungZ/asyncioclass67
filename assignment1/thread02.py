# running a function with arguments in another thread
from time import sleep, ctime
from threading import Thread
def task(sleep_time,message):
    sleep(sleep_time)
    print(f'{ctime()}{message}')

thread = Thread(target=task,args=(1.2,'New message from another thread'))
thread.start()
print(f'{ctime()}Waitting for the thread...')
thread.join()