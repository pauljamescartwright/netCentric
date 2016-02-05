# multiThreaded.py
import threading
import time
import random


def BigLoop(p, lock):
    for num in range(0, 100):
        lock.acquire()
        print('Player ' + str(p) + ':  ' + str(num))
        lock.release()
        time.sleep(random.randint(1,3))


def multiplayer():
    lock = threading.Lock()
    for playerNum in range(0, 3):
        threading.Thread(target=BigLoop, args=(playerNum, lock)).start()

        # BigLoop(playerNum)


multiplayer()
