from __future__ import print_function

class A(object):

    _req = ['a']

    def hello_a(self):
        print(self._req)



class B(A):

    #_req = ['b']

    def hello_b(self):
        print(self._req)


if __name__ == '__main__':
    a = A()
    a.hello_a()  # a
    b = B()
    b.hello_a() # b
    b.hello_b() # b


    print hello
