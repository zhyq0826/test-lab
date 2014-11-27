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

@profile
def test_reference_cycle():
    import gc
    import time
    MAX = 10000
    LIFE = 15

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
    a = None
    b = None
    logger.debug('a and b is deleted')

    time.sleep(LIFE)

if __name__ == '__main__':
    test_reference_cycle()
