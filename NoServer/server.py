#! python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from sys import argv
from collections import namedtuple
from os import path

class MimeType:
    html = 'text/html'
    js = 'text/javascript'
    css = 'text/css'
    jpg = 'image/jpeg'
    gif = 'image/gif'
    image = ('image/jpeg', 'image/gif')
    text = ('text/html', 'text/css', 'text/javascript')
    ico = 'NotImplemented'


class MungoServer(BaseHTTPRequestHandler):

    content_path = path.dirname(path.realpath(__file__))
    collection = ''

    def __set_headers(self, response):
        self.send_response(response.code)
        self.send_header('Content-type', response.type)
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        mime = getattr(MimeType, path.split('.')[-1], 'text/html')
        if mime in MimeType.image:
            try:
                data_fp = open(f'{MungoServer.content_path}/{path}', 'rb')
            except IOError:
                print(f'Not found {path}')
                self.__set_headers(namedtuple('response', ('code', 'type'))('404', 'text/html'))
                self.wfile.write(bytes(f'File not found {MungoServer.content_path}/{path.split("/")[-1]}'))
            else:
                self.__set_headers(namedtuple('response', ('code', 'type'))(200, mime))
                self.wfile.write(data_fp.read())
                data_fp.close()
        elif mime in MimeType.text:
            try:
                if not path or path == '/':
                    file = f'{MungoServer.content_path}/{MungoServer.collection}.html'
                else:
                    file = f'{MungoServer.content_path}/{path}'
                data_fp = open(file, 'rb')
            except IOError:
                self.__set_headers(namedtuple('response', ('code', 'type'))('404', 'text/html'))
                self.wfile.write(bytes(f'File not found{file}'))
                data_fp.close()
            else:
                data = data_fp.read()
                data_fp.close()
                self.__set_headers(namedtuple('response', ('code', 'type'))(200, mime))
                self.wfile.write(data)

    def do_POST(self):
        pass

    @staticmethod
    def run(host='', port=9090):
        if port is None:
            port = 9090
        http_server = (host, port)
        print(http_server)
        httpd = HTTPServer(http_server, MungoServer)
        try:
            print(f'Starting server on: {host or "http://localhost"}{":"+str(port) if port != 80 else ""}')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('Bye!')
            httpd.shutdown()
            exit()


if __name__ == '__main__':
    if len(argv) <2 or len(argv) > 3:
        print('Usage: MungoServer <repo> [<port>]')
        exit(1)
    MungoServer.collection += argv[1]
    port = int(dict(enumerate(argv)).get(2))
    MungoServer.run(port=port)
