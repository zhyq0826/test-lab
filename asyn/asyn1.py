import time
import tornado.web
import tornado.ioloop
from tornado import httpclient
import tornado.httpclient
import tornado.gen
import tornado.httpserver
import tornado.autoreload
from tornado.options import define, options
import tornado.options

class PretendService(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        """Pretend some work is being done by sleeping for 500ms"""
        ioloop = tornado.ioloop.IOLoop.instance()
        ioloop.add_timeout(time.time()+0.5, self.on_response)

    def on_response(self):
        self.finish()

# pretend_service_url = 'http://127.0.0.1:8888/external-api'
pretend_service_url = 'http://baidu.com'

class MainHandlerBlocking(tornado.web.RequestHandler):
    def get(self):
        req = httpclient.HTTPRequest(pretend_service_url, method='GET')
        # we could use something like requests or urllib here
        client = tornado.httpclient.HTTPClient()
        response = client.fetch(req)
        self.write('blocking')
        # do something with the response


class MainHandlerAsync(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        req = httpclient.HTTPRequest(pretend_service_url, method='GET')
        client = tornado.httpclient.AsyncHTTPClient()
        # don't let the yield call confuse you, it's just Tornado helpers to make
        # writing async code a bit easier. This is the same as doing
        # client.fetch(req, callback=_some_other_helper_function)
        response = yield tornado.gen.Task(client.fetch, req)
        ### do something with the response ###
        self.write('async')
        self.finish()


application = tornado.web.Application([
    (r"/async", MainHandlerAsync),
    (r"/external-api", PretendService),
    (r"/blocking", MainHandlerBlocking)
])

if __name__ == "__main__":
    define("port", default=8888, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.autoreload.start()
    tornado.ioloop.IOLoop.instance().start()