from tornado import httpserver
from tornado import ioloop
 
def handle_request(request):
    message = "You requested %s\n" % request.uri
    request.write("HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % (
                 len(message), message))
    request.finish()
 
http_server = httpserver.HTTPServer(handle_request)
http_server.bind(8888)
http_server.start()
ioloop.IOLoop.instance().start()