from threading import Lock, Thread
import time

database_val = 0

def increase(lock):
    global database_val

    lock.acquire()
    

    localCopy = database_val

    localCopy += 1

    time.sleep(0.1)

    database_val = localCopy
    
    lock.release()



if __name__ == "__main__":
    print("start value:",database_val)
    lock = Lock()

    thread1 = Thread(target=increase , args=(lock,))
    thread2= Thread(target=increase , args=(lock ,))
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("end value" , database_val)

