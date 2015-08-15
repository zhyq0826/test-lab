import BaseHTTPServer
import SocketServer
import time


class User(object):
    def save(self):
        time.sleep(0.2)

    def send_email(self):
        time.sleep(0.6)

    def social_api(self):
        time.sleep(2)


class SynServer(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self, *args, **kwargs):
        user = User()
        user.save()
        user.send_email()
        user.social_api()
        self.send_response(200, message='ok')
        self.end_headers()



def run():
    port = 8888
    Handler = SynServer

    httpd = SocketServer.TCPServer(("", port), Handler)

    print('server at port: %s'%port)
    httpd.serve_forever()


if __name__ == '__main__':
    run()