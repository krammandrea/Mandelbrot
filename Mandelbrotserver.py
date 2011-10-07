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
	    self.do_GET_Mandelbrot_png()
	elif self.path.endswith("arrow_right.png"):
	    self.do_GET_arrow_right_png()
	elif self.path.endswith("arrow_left.png"):
            self.do_GET_arrow_left_png()
	elif self.path.endswith("arrow_up.png"):
            self.do_GET_arrow_up_png()
	elif self.path.endswith("arrow_down.png"):
            self.do_GET_arrow_down_png()
	elif self.path.endswith("circle.png"):
            self.do_GET_circle_png()
	elif '?x'in self.path:
	    self.do_GET_new_coordinate()
	else:
	    self.send_response(404)
#TODO self.send_header("Content-type","application/x-download")
    def do_GET_main_page(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
	self.show_main_page()
	
    def show_main_page(self):

	main_page_html = open("Mandelbrotserver.html","r")
	self.wfile.write(main_page_html.read())



    def do_GET_Mandelbrot_png(self):

	self.send_response(200)
	self.send_header("Content-type","image/png")
	self.end_headers()	
	pngfile = open("MandelbrotImg/Mandelbrot.png","rb")
	self.wfile.write(pngfile.read())
	pngfile.close()

    def do_GET_arrow_right_png(self):

        self.send_response(200)
        self.send_header("Content-type","image/png")
        self.end_headers()      
        pngfile = open("MandelbrotImg/arrow_right.png","rb")
        self.wfile.write(pngfile.read())
        pngfile.close()

    def do_GET_arrow_left_png(self):

        self.send_response(200)
        self.send_header("Content-type","image/png")
        self.end_headers()      
        pngfile = open("MandelbrotImg/arrow_left.png","rb")
        self.wfile.write(pngfile.read())
        pngfile.close()

    def do_GET_arrow_up_png(self):

        self.send_response(200)
        self.send_header("Content-type","image/png")
        self.end_headers()      
        pngfile = open("MandelbrotImg/arrow_up.png","rb")
        self.wfile.write(pngfile.read())
        pngfile.close()

    def do_GET_arrow_down_png(self):

        self.send_response(200)
        self.send_header("Content-type","image/png")
        self.end_headers()      
        pngfile = open("MandelbrotImg/arrow_down.png","rb")
        self.wfile.write(pngfile.read())
        pngfile.close()

    def do_GET_circle_png(self):

        self.send_response(200)
        self.send_header("Content-type","image/png")
        self.end_headers()      
        pngfile = open("MandelbrotImg/circle.png","rb")
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

