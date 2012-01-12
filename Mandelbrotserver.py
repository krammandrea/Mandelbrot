import string
import re
import BaseHTTPServer
import Mandelbrot

HOST_NAME = '' # empty because using http://localhost
PORT_NUMBER = 8080

class ImageAdministrator():
    def __init__(self):
	self.height = 1000
	self.width = 1000
	self.maxiteration = 10
	self.offsetx = self.height/2
	self.offsety = self.width/2
	self.zoomfactor = 1
	self.colorscheme = [(0,0,0),(51,102,51),(51,102,77),(51,102,102),(51,77,102),(51,51,102),(77,51,102),(102,51,102),(102,51,77),(102,51,51),(102,77,51),(102,102,51),(77,102,51)] #GREEN

    def reset_to_default(self):
	pass
    def change_offset_and_zoom(self, new_x, new_y):
	self.offsetx 
    def change_zoom(self):
	pass
    def change_offset(self):
	pass
    def change_colorscheme(self):
	pass
    def change_maxiteration(self):
	pass
    def get_parameters(self):
	return self.height, self.width, self.maxiteration, self.offsetx, self.offsety, self.zoomfactor, self.colorscheme
    def save_parameters_to_file(self):
	pass
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
	if self.path.endswith("index.html"):
	    self.do_GET_main_page()
	elif self.path.endswith("/"):
	    self.get_main_page()
	#TODO only if ?x AND zoom_offset
	elif '?x'in self.path:
	    new_x,new_y = self.get_new_coordinate()

	    #calculate absolute zoomfactor and offset from all the relative factors in the recent browsing history
	    Mandelbrot.calculate_mandelbrot()	
	    #imageheight,imagewidth: pixelsize of the image
            #maxiteration: directly correlated to the duration of the calculation ?when does it get too long
            #offsetx, offsety: new center of the reference image
            #zoomfactor: absolute zoomfactor range 1 to indefinitely
            #colorscheme: 12 elements, default value is green	
	    self.get_main_page()   
	#TODO /zoom_in /zoom_out and /zoom
	elif self.path.find("/MandelbrotImg/") >=0:
	    #extract the name of the requested picture
	    #do_GET_image("Imagename")
	    self.get_image(self.path.rpartition("MandelbrotImg/")[-1])
	    
	else:
	    self.send_response(404)
#TODO self.send_header("Content-type","application/x-download")
    def get_main_page(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
	main_page_html = open("Mandelbrotserver.html","r")
	self.wfile.write(main_page_html.read())

    def get_image(self,imagename):
	
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

    def get_new_coordinate(self):
	#extract new coordinates
	    # find the block of numbers after 'x=' and 'y='
	regExp = re.compile(r"x=([0-9]+)")
	new_x= string.atoi(regExp.findall(self.path)[0])
	regExp = re.compile(r"y=([0-9]+)")
        new_y = string.atoi(regExp.findall(self.path)[0]) 
	return new_x, new_y
 
	
	
if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

