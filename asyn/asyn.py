import time
import datetime
from tornado.concurrent import return_future
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import gen

class AsynUser(object):

    @return_future
    def save(self, callback=None):
        time.sleep(0.02)
        result = datetime.datetime.now()
        callback(result)

    @return_future
    def send_email(self, callback=None):
        time.sleep(0.06)
        result = datetime.datetime.now()
        callback(result)

    @return_future
    def social_api(self, callback=None):
        time.sleep(0.2)
        result = datetime.datetime.now()
        callback(result)



class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/', UserHandler),
        ]

        tornado.web.Application.__init__(self, handlers=handlers)


class UserHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        user = AsynUser()
        response = yield (user.save())

        response2 = yield (user.send_email())
        response3 = yield (user.social_api())
        self.finish()


def main():
    port = 8888
    http_server = tornado.httpserver.HTTPServer(Application())
    print('server at port: %s'%port)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()