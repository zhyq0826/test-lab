__author__ = 'zhyq'

import time
import threading
import os
import thread

def loop0():
    print 'start loop0 ', time.ctime()
    time.sleep(4)
    print 'end loop ', time.ctime()

def loop1():
    print 'start loop1 ', time.ctime()
    time.sleep(2)
    print 'end loop1 ', time.ctime()

def main():
    print 'main start at ', time.ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    time.sleep(6)
    print 'all done ', time.ctime()

def loop(nloop, sec, lock):
    print 'start loop', nloop, ' at ', time.ctime()
    time.sleep(sec)
    print 'end loop', nloop, ' at ', time.ctime()
    lock.release()


def main2():
    print 'starting at ', time.ctime()
    locks = []
    loops = [4, 2]
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        print lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass

    print 'all done at', time.ctime()

def main3():
    print 'starting at ', time.ctime()
    threads = []
    loops = [4, 2]
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()




if __name__ == '__main__':
    main2()