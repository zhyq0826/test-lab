
from Queue import Queue
import multiprocessing

class Base(object):

    def __init__(self, queue):
        self.queue = queue

    def do_work(self):
        while 1:
            print('base')
            self.queue.put('hello')


class B(Base):

    def __init__(self, queue):
        self.queue = queue

    def do_work(self):
        while 1:
            print('B')
            #print(self.queue.get())

import  threading



if __name__ == '__main__':
    q = Queue()
    print(id(q))
    base = Base(q)
    p1 = multiprocessing.Process(target=base.do_work)
    p1.start()
    p1.join()
    print(id(q))
    b = B(q)
    p2 = multiprocessing.Process(target=b.do_work)
    p2.start()
    p2.join()
    print(id(q))