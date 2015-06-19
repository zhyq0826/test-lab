__author__ = 'zhyq'

import threading

import Queue



def hello():
    print 'hello'
    raise SystemExit()

def hello2(q=None):
    import time
    while 1:
        print 'hello2'
        time.sleep(5)


if __name__ == '__main__':
    t1 =threading.Thread(target=hello)
    t1.start()
    t2 = threading.Thread(target=hello2)
    t2.start()