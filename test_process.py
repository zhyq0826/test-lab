__author__ = 'zhyq'

import multiprocessing
import time

def hello():
    import time
    time.sleep(1)
    print('hello world')

def main1():
    t = multiprocessing.Process(target=hello)
    t.daemon
    t.start()
    #t.join()
    print 'asdf'

class ActivePool(object):

    def __init__(self):
        self.mgr = multiprocessing.Manager()
        self.active = self.mgr.list()
        self.lock = multiprocessing.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)

    def __str__(self):
        with self.lock:
            return str(self.active)


def workers(s, pool):
    name = multiprocessing.current_process().name
    with s:
        pool.makeActive(name)
        #print 'now runing: %s' % str(pool)
        time.sleep(3)
        pool.makeInactive(name)

def main2():
    pool = ActivePool()
    s = multiprocessing.Semaphore(3)
    jobs = [multiprocessing.Process(target=workers, name=str(i), args=(s, pool)) for i in range(10)]

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()
        print 'now runing', str(pool)

if __name__ == '__main__':
    def do_calculation(data):
        #print 'starting ', multiprocessing.current_process().name
        return data*2

    def start_init():
        pass
        #print 'starting ', multiprocessing.current_process().name

    inputs = list(range(20))
    start = time.time()
    pool = multiprocessing.Pool(processes=4, initializer=start_init)
    pool_outputs2 = pool.map_async(do_calculation, inputs)
    pool.close()
    pool.join()
    #one = map(do_calculation, inputs)
    #one = map(do_calculation, inputs)
    print time.time()-start

