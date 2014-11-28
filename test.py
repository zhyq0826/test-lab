from __future__ import print_function

import logging
from logging import StreamHandler

from memory_profiler import profile

logger = logging.getLogger()
logger.addHandler(StreamHandler())
logger.setLevel(logging.DEBUG)

def glow_pyconf_ppt():
    import requests
    for i in range(1, 24):
        s = requests.get('http://boolan.com/Courses/a4e31043-f830-49ff-8488-0801a84dcc0c/slide%s.jpg'%i)
        f = open("/home/zhyq/slide%s.jpg"%i,"w")
        f.write(s.content)

#@profile
def test_reference_cycle():
    import gc
    import time
    MAX = 10
    LIFE = 10

    class A(object):

        def __init__(self, b=None):
            self.b = b
            self.l = []
            self.init()
        
        def init(self):
            for i in range(0, MAX):
                self.l.append('abcdefgaaaaaaa')
            

    class B(object):

        def __init__(self, a=None):
            self.a = a
            self.l = []
            self.init()
    
        def init(self):
            for i in range(0, MAX):
                self.l.append('gfedcbaaaaaaaa')
    
    logger.debug('start generate object')
    a = A()
    b = B()
    logger.debug('object exists last %ss'%LIFE)

    time.sleep(LIFE)
    
    #a.b = b
    #b.a = a
    logger.debug('delete a, b')
    a.l = None
    b.l = None
    a = None
    b = None
    del a
    del b
    logger.debug('a and b is deleted')

    logger.debug('wait %s to collect'%LIFE)
    time.sleep(LIFE)
    gc.collect()
    logger.debug('collect is finished')

    time.sleep(LIFE)

def test_inspect():
    import inspect

    def hello(route, objid, val=10, *args, **kwargs):
        import time
        time.sleep(100)
        print('hello world')

    print(inspect.getargspec(hello))
    #print(inspect.formatargspec())
    print(inspect.getcallargs(hello, 'paper', 'id'))

if __name__ == '__main__':
    test_reference_cycle()
