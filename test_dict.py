__author__ = 'zhyq'

from tornado.util import ObjectDict
class A(object):

    __slots__ = ['_data', '_dirty']

    def __init__(self):
        self._dirty = False
        self._data = ObjectDict({'a':10})

    def __getitem__(self, name):
        return self._data.get(name, None)

    def __setitem__(self, name, value):
        self._data[name] = value
        self._dirty = True

    def __delitem__(self, name):
        del self._data[name]
        self._dirty = True

    def __contains__(self, name):
        return name in self._data

    def __len__(self):
        return len(self._data)

    def __getattr__(self, name):
        print('getattr %s' % name)
        return getattr(self._data, name)

    def __setattr__(self, name, value):
        print('__setattr__ %s '%name)
        if name in self.__slots__:
            print('setattr slots %s'%name)
            super(A, self).__setattr__(name, value)
        else:
            print('setattr data %'%name)
            self._dirty = True
            setattr(self._data, name, value)

    def __delattr__(self, name):
        print('__delattr__')
        delattr(self._data, name)
        self._dirty = True

    def __iter__(self):
        for key in self._data:
            yield key

    def __repr__(self):
        return str(self._data)


if __name__ == '__main__':
    a = A()
    # #a._dirty
    # #a.a
    print(a)
    print(a.update())
    #a.update({'10': 1})