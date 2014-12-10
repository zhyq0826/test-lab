#-*- coding:utf-8 -*-
from __future__ import print_function

import logging
from logging import StreamHandler

from memory_profiler import profile
import requests

logger = logging.getLogger()
logger.addHandler(StreamHandler())
logger.setLevel(logging.DEBUG)


def jing_fm_api():
    fav_url = 'http://jing.fm/api/v1/music/fetch_fav'
    cookies = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2',
        'Connection':'keep-alive',
        'Content-Length':'34',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'__utma=229842311.1901801531.1417421539.1417421539.1417421798.2; __utmc=229842311; __utmz=229842311.1417421798.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=jingfm3.0',
        'Host':'jing.fm',
        'Jing-A-Token-Header':'PAMKVRZRUFRSQkdPRFsOXVgNXFA=',
        'Jing-R-Token-Header':'eFFeVBlFBAkc',
        'Origin':'http://jing.fm',
        'Referer':'http://jing.fm/beta/',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        }

    s = requests.post(fav_url, cookies=cookies, data={'uid': 280377, 'ouid': 280377, 'st': 0, 'ps': 36})
    print(s.content)


def boolan_com_ppt():
    slide_id = '7cc9f806-52c7-4c58-aa05-f911f2a2d532'
    for i in range(24, 48):
        s = requests.get('http://boolan.com/Courses/%s/slide%s.jpg'%(slide_id, i))
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
    jing_fm_api()
