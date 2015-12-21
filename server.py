# coding:utf-8
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define, options
from application import application

define("port", default=8080)


def main():
    tornado.options.parse_command_line()
    app = application()
    app.listen(options.port)
    print('Development server is running at http://127.0.0.1:%s/' % options.port)
    print('Quit the server with Control-C')
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
