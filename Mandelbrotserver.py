import string
import re
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
	elif '?x'in self.path:
	    self.do_GET_new_coordinate()
	else:
	    self.send_response(404)

    def do_GET_main_page(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
	self.show_main_page()

    def show_main_page(self):
	self.wfile.write("<html><head><title>Mandelbrot</title></head>")
        self.wfile.write("<body><p>This is a test.</p>")
        #self.wfile.write("<img src='Mandelbrot.png'>")
        self.wfile.write("<form action='/' method=get><input type=image src='/Mandelbrot.png' alt='click for zoom' border=0></form>")
	# If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        #self.wfile.write("<p>You accessed path: %s</p>" % self.path)
        self.wfile.write("</body></html>")
        print self.path



    def do_GET_Mandelbrot(self):

	self.send_response(200)
	self.send_header("Content-type","image/png")
	self.end_headers()	
	pngfile = open("Mandelbrot.png","rb")
	self.wfile.write(pngfile.read())
	pngfile.close()

    #handles http://localhost:8080/?x=658&y=586 requests
    def do_GET_new_coordinate(self):
	#extract new coordinates
	    # find the block of numbers after 'x=' and 'y='
	regExp = re.compile(r"x=([0-9]+)")
	new_x= string.atoi(regExp.findall(self.path)[0])
	regExp = re.compile(r"y=([0-9]+)")
        new_y = string.atoi(regExp.findall(self.path)[0]) 
	self.end_headers()
	#TODO calculate_mandelbrot()	
	self.show_main_page()   
 
if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

