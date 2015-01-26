__author__ = 'zhyq'

import multiprocessing

def hello():
    import time
    time.sleep(1)
    print('hello world')

if __name__ == '__main__':
    t = multiprocessing.Process(target=hello)
    t.daemon
    t.start()
    #t.join()
    print 'asdf'