"""Interprets the user clicks on the website and relates the parameter to the Mandelbrot calculating class
"""
import string
import re
import BaseHTTPServer
import mandelbrot

HOST_NAME = '' # empty because using http://localhost
PORT_NUMBER = 8080

#TODO: put class in new file, find name, find the big picture, comment pydoc, comment variables, is it a module?
class ImageAdministrator():
    """stores the current parameters of the image which the user changes until he is satisfied and saves the image and the accompaning calculating data to file""" 
    GREEN= [(0,0,0),(51,102,51),(51,102,77),(51,102,102),(51,77,102),(51,51,102),(77,51,102),(102,51,102),(102,51,77),(102,51,51),(102,77,51),(102,102,51),(77,102,51)]
    #"""default colorscheme in green"""
    def __init__(self):
	self.height = 600
	self.width = 600
	self.maxiteration = 10
        self.xabsolutestart = -2.0
        self.xabsoluteend = 2.0
        self.yabsolutestart = -2.0
        self.yabsoluteend = 2.0
	self.colorscheme = self.GREEN	
        print 'initializing' 
    def change_imagesize(self,new_width, new_height):
#TODO remember to adjust zoomfactor if zoom=1 and image not quadratic
        """adjust dependent offsetabsolute"""
        pass
    def reset_to_default(self):
	pass
    def change_zoom(self,zoom_relative):
        #zoom_relative has a value of 1 to 100 with 1 being the original image


	pass
    def change_offset_and_zoom(self, new_center_x, new_center_y,zoom_on_click):
        print self.xabsolutestart, self.xabsoluteend
        xabsoluteoffset = (new_center_x - self.width/2)*(self.xabsoluteend - self.xabsolutestart)/self.width
        yabsoluteoffset = (new_center_y - self.height/2)*(self.yabsoluteend - self.yabsolutestart)/self.height
	self.xabsolutestart += xabsoluteoffset
	self.yabsolutestart += yabsoluteoffset
        self.xabsoluteend += xabsoluteoffset
        self.yabsoluteend += yabsoluteoffset       
        
        
        print self.xabsolutestart, self.xabsoluteend, zoom_on_click,( self.xabsoluteend-self.xabsolutestart)
        #the zoom_on_click halfs the orignal size while the center stays the same
	self.xabsolutestart  += 0.5/zoom_on_click*(self.xabsoluteend-self.xabsolutestart)
	self.yabsolutestart  += 0.5/zoom_on_click*(self.yabsoluteend-self.yabsolutestart)
	self.xabsoluteend    -= 0.5/zoom_on_click*(self.xabsoluteend-self.xabsolutestart)
	self.yabsoluteend    -= 0.5/zoom_on_click*(self.yabsoluteend-self.yabsolutestart)

        print self.xabsolutestart, self.xabsoluteend
    def change_colorscheme(self):
	pass
    def change_maxiteration(self):
	pass
    def get_parameters(self):
	return self.height, self.width, self.maxiteration, self.xabsolutestart, self.xabsoluteend, self.yabsolutestart, self.yabsoluteend, self.colorscheme
    def save_parameters_to_file(self):
	pass


#TODO rename file, restructre if/else part and add comments what the user actions are 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    ZOOM_ON_CLICK= 2
    def __init__(self,request, client_adress,server):
        self.imageAdministrator = server.imageAdministrator
        BaseHTTPServer.BaseHTTPRequestHandler.__init__(self,request,client_adress,server)
#"""standard zoom when clicking into the image"""
#TODO hash table for url path instead of if elif
    def do_GET(self):
	if self.path.endswith("index.html"):
	    mandelbrot.calculate_mandelbrot()
	    self.do_GET_main_page()
	elif self.path.endswith("/"):
	    mandelbrot.calculate_mandelbrot()
	    self.get_main_page()
	#TODO only if ?x AND zoom_offset
	elif '?x'in self.path:
	    """when clicking into the image the new image will be calculated centered around the clicked point"""
	    new_x,new_y = self.get_new_coordinate()
	    self.imageAdministrator.change_offset_and_zoom(new_x,new_y,self.ZOOM_ON_CLICK)
	    mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
	    self.get_main_page()   
	#TODO /zoom_in /zoom_out and /zoom
	elif self.path.find("/images/") >=0:
	    #extract the name of the requested picture
	    #do_GET_image("Imagename")
	    self.get_image(self.path.rpartition("images/")[-1])
	elif self.path.find("save") >=0:
            self.download_fractal_param_dat()
               
	else:
	    self.send_response(404)


#TODO self.send_header("Content-type","application/x-download")
    def get_main_page(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
	main_page_html = open("main.html","r")
	self.wfile.write(main_page_html.read())

#TODO else only after imagename not existent 
    def get_image(self,imagename):
    #responds to a request for an image by checking for the file in folder /images	
	if imagename.endswith(".png"):
	    self.send_response(200)
	    self.send_header("Content-type","image/png")
	    self.end_headers()	
	    pngfile = open("images/"+imagename,"rb")
	    self.wfile.write(pngfile.read())
	    pngfile.close()
	#elif: expand to other imagedatatypes if necessary here
	else:
	    self.send_response(404)

    #handles http://localhost:8080/?x=658&y=586 requests
    #TODO should handle http://localhost:8080/zoom_offset?x=658&y=586 requests


    def download_fractal_param_dat(self):
        self.send_response(200)
        self.send_header("Content-type","application/x-download")
        self.send_header("Content-disposition","attachement; filename='filenametest'")
        self.end_headers()
        
        fractal_para=self.imageAdministrator.get_parameters()
        fractal_para_str=repr(fractal_para)

        self.wfile.write(fractal_para_str)


    def get_new_coordinate(self):
    #extract new center of image after the user click out of the url
	# find the block of numbers after 'x=' and 'y='
	regExp = re.compile(r"x=([0-9]+)")
	new_x= string.atoi(regExp.findall(self.path)[0])
	regExp = re.compile(r"y=([0-9]+)")
        new_y = string.atoi(regExp.findall(self.path)[0]) 
	return new_x, new_y
 
	
	
if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    #piggybacking imageadministrator into Myhandler instead of using it globally
    #idea: this could be a singleton pattern    
    httpd.imageAdministrator = ImageAdministrator()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

