import os
import sys
from tornado.util import ObjectDict

import redis

import time

r = redis.StrictRedis()

def main():
    return [0-i for i in range(0, 10000000)]

def main2():
    return [int('-%s'%i) for i in range(0, 10000000)]

s = ['s','j']

class Cache(object):

    def __getattr__(self, item):
        return getattr(r, item)

    def __setattr__(self, key, value):
        if getattr(r, key, None):
            raise AttributeError('sd')

        return setattr(Cache, key, value)

    def get_con(self):
        print 'cache hello'

class ListCache(Cache):
    pass

class Conn(object):

    def get_con(self):
        print 'conn hello'


class Comment(Conn, ListCache):
    pass

if __name__ == '__main__':
    c = Comment()
    print c.get
    print r.type('h')
    print r.type('s')=='none'

