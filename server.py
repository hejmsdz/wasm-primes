#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer

PORT = 8000

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    pass

Handler.extensions_map['.wasm'] = 'application/wasm'

httpd = SocketServer.TCPServer(('', PORT), Handler)

print 'serving at port', PORT
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print 'exiting'
    httpd.shutdown()
