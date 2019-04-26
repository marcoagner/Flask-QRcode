'''

 Copyright (C) 2016 Marco Agner

 This file is part of Flask-QRcode.

 Flask-QRcode is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 Flask-QRcode is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with Flask-QRcode.  If not, see <http://www.gnu.org/licenses/>.

'''
import http.server
import socketserver
import threading


class TestServer(socketserver.TCPServer):
    allow_reuse_address = True


def start_test_server(port=5000):
    handler = http.server.SimpleHTTPRequestHandler
    httpd = TestServer(("", port), handler)
    httpd_thread = threading.Thread(target=httpd.serve_forever)
    httpd_thread.setDaemon(True)
    httpd_thread.start()
