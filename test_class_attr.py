class Base(object):

    _instance = {}

    field = {'h': 10}

    @staticmethod
    def instance(key):
        if not Base._instance.get(key):
            Base._instance[key] = 11

        return Base._instance[key]



class A(Base):
    pass


class B(Base):
     Base.field.update({'k': 10})


if __name__ == '__main__':
    a = A()
    b = B()
    b.instance('hello')
    a.instance('h')
    print(b._instance) 
    print(a._instance)
    print a._instance == b._instance
    print(b.field)
    print(Base.field)
