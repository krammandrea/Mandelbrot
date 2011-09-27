
import BaseHTTPServer


HOST_NAME = '' # empty because using http://localhost
PORT_NUMBER = 8080


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
	if self.path.endswith("index.html"):
	    self.do_GET_main_page()
	elif self.path.endswith("/"):
	    self.do_GET_main_page()
	elif self.path.endswith("Mandelbrot.png"):
	    self.do_GET_Mandelbrot()
	else:
	    self.send_response(404)

    def do_GET_main_page(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Mandelbrot</title></head>")
        self.wfile.write("<body><p>This is a test.</p>")
	self.wfile.write("<img src='Mandelbrot.png'>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        self.wfile.write("<p>You accessed path: %s</p>" % self.path)
        self.wfile.write("</body></html>")
	print self.path

    def do_GET_Mandelbrot(self):

	self.send_response(200)
	self.send_header("Content-type","image/png")
	self.end_headers()	
	pngfile = open("Mandelbrot.png","rb")
	self.wfile.write(pngfile.read())
	pngfile.close()
    
if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

