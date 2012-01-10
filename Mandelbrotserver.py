import string
import re
import BaseHTTPServer
import Mandelbrot

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
	#TODO only if ?x AND zoom_offset
	elif '?x'in self.path:
	    self.do_GET_new_coordinate()
	#TODO /zoom_in /zoom_out and /zoom
	elif self.path.find("/MandelbrotImg/") >=0:
	    #extract the name of the requested picture
	    #do_GET_image("Imagename")
	    self.do_GET_image(self.path.rpartition("MandelbrotImg/")[-1])
	    
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

    def do_GET_image(self,imagename):
	
	if imagename.endswith(".png"):
	    self.send_response(200)
	    self.send_header("Content-type","image/png")
	    self.end_headers()	
	    pngfile = open("MandelbrotImg/"+imagename,"rb")
	    self.wfile.write(pngfile.read())
	    pngfile.close()
	#elif: expand to other imagedatatypes if necessary here
	else:
	    self.send_response(404)

    #handles http://localhost:8080/?x=658&y=586 requests
    #TODO should handle http://localhost:8080/zoom_offset?x=658&y=586 requests

    def do_GET_new_coordinate(self):
	#extract new coordinates
	    # find the block of numbers after 'x=' and 'y='
	regExp = re.compile(r"x=([0-9]+)")
	new_x= string.atoi(regExp.findall(self.path)[0])
	regExp = re.compile(r"y=([0-9]+)")
        new_y = string.atoi(regExp.findall(self.path)[0]) 
	#calculate absolute zoomfactor and offset from all the relative factors in the recent browsing history
	Mandelbrot.calculate_mandelbrot()	
	
	self.do_GET_main_page()   
 
	
	
if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

