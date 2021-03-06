import string,re,math,urlparse
import BaseHTTPServer
import mandelbrot,coloralg,imageAdministrator

HOST_NAME = '' # empty because using http://localhost
PORT_NUMBER = 8080


#TODO rename file, restructre if/else part and add comments what the user actions are 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
    Interprets the user clicks on the website and relates the parameter to the 
    Mandelbrot calculating class
    """
    ZOOM_ON_CLICK= 2.0
    OFFSETFACTOR = 0.20 #image section moves by 20%    
    ZOOMRELATIVE = 2.0    
        

    def __init__(self,request, client_adress,server):
        self.imageAdministrator = server.imageAdministrator
        self.colorAlg = server.colorAlg
        BaseHTTPServer.BaseHTTPRequestHandler.__init__(self,request,client_adress,server)


#TODO hash table for url path instead of if elif
    def do_GET(self):
        query  = urlparse.parse_qs(urlparse.urlparse(self.path).query)
        #extract the requested url path and strip the first "/" for later use with open()
        url_path = string.lstrip(urlparse.urlparse(self.path).path,"/")

	if "index.html" in url_path:
	    mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
	    self.get_main_page()

	elif self.path.endswith("/"):
	    mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
	    self.get_main_page()
#TODO only /images or /jscolor
	elif ".png" in url_path or ".gif" in url_path:
            self.get_image(url_path)

        elif "style" in url_path:
            self.get_css(url_path)

        elif ".js"in url_path:
            self.get_javascript(url_path)

        elif "change_color" in url_path:
	    if(self.imageAdministrator.isColorInputValid(query['col'])):
		self.imageAdministrator.change_colorscheme(query['col'])
		self.colorAlg.initcolorscheme(query['col'][1:len(query['col'])])
		mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
	    else:
		pass #TODO put useralert on mainpage
	    self.get_main_page()

        elif "change_iteration" in url_path:
	    iterationString = query["iter"][0]
	    if self.imageAdministrator.isIterationInputValid(iterationString):
		self.imageAdministrator.change_maxiteration(int(iterationString))
		mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
	    else:
		pass	#TODO put useralert on mainpage
	    self.get_main_page()

        elif "change_size" in url_path:
	    if (self.imageAdministrator.isSizeInputValid(query['pxwidth'][0]) and 
		self.imageAdministrator.isSizeInputValid(query['pxheight'][0])):
		self.imageAdministrator.change_imagesize(int(query['pxwidth'][0]),int(query['pxheight'][0]))
		mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
	    else:
		pass	#TODO put useralert on mainpage
	    self.get_main_page()
		
        elif "section" in url_path:
            new_borderlines = self.get_borderlines(query)
            self.imageAdministrator.change_section(new_borderlines)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page()

	elif 'zoom_offset' in url_path:
	    """
	    when clicking into the image the new image will be calculated centered 
	    around the clicked point
	    """
	    new_x,new_y = self.get_new_coordinate(query)
	    self.imageAdministrator.change_offset_and_zoom(new_x,new_y,self.ZOOM_ON_CLICK)
	    mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
	    self.get_main_page()   

	    """
	    when clicking on arrow buttons the new image section will move to the 
	    corresponding direction
	    """
        elif 'offset_right' in url_path:
            self.imageAdministrator.change_offset(self.OFFSETFACTOR,0)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 

        elif 'offset_left' in url_path:
            self.imageAdministrator.change_offset(-self.OFFSETFACTOR,0)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 

        elif 'offset_up' in url_path:
            self.imageAdministrator.change_offset(0,-self.OFFSETFACTOR)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 

        elif 'offset_down' in url_path:
            self.imageAdministrator.change_offset(0,self.OFFSETFACTOR)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 

        elif 'zoom_in' in url_path:
            self.imageAdministrator.change_zoom(self.ZOOMRELATIVE)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 

        elif 'zoom_out' in url_path:
            self.imageAdministrator.change_zoom(1/self.ZOOMRELATIVE)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 

        elif 'zoom' in url_path:
            self.imageAdministrator.change_zoom(self.ZOOMRELATIVE)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 

	elif "save" in url_path:
            self.download_fractal_param_dat()

	else:
	    self.send_response(404, "not in alternative list")


#TODO self.send_header("Content-type","application/x-download")
    def get_main_page(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
	main_page_html = open("main.html","r")
	self.wfile.write(main_page_html.read())

#TODO catch files not openable
    def get_css(self,csspath):
        if csspath.endswith(".css"):
            self.send_response(200)
            self.send_header("Content-type","text/css")
            self.end_headers()
            cssfile = open(csspath,"rb")
            self.wfile.write(cssfile.read())
            cssfile.close()            
        else:
            self.send_response(404)    
	    print "no .css file found"


    def get_javascript(self,jscolorpath):
        if jscolorpath.endswith(".js"):
            self.send_response(200)
            self.send_header("Content-type","text/javascript")
            self.end_headers()
            jscolorfile = open(jscolorpath,"rb")
            self.wfile.write(jscolorfile.read())
            jscolorfile.close()
        else:
            self.send_response(404)        


    def get_borderlines(self,querydict):
	new_borderlines = [0.0 for x in range(4)]
	new_borderlines[0] = float(querydict["xs"][0])
	new_borderlines[1] = float(querydict["xe"][0])
	new_borderlines[2] = float(querydict["ys"][0])
	new_borderlines[3] = float(querydict["ye"][0])
#        regExp = re.compile("(-?[0-9]+\.?[0-9]*)")
#        new_borderlines = [float(corner) for corner in regExp.findall(sectionstring)]

        return new_borderlines

#TODO else only after imagename not existent 
    def get_image(self,imagepath):
        """
        responds to a request for an image by checking for the file at the given path	
        """
	if imagepath.endswith(".png"):
	    self.send_response(200)
	    self.send_header("Content-type","image/png")
	    self.end_headers()	
	    pngfile = open(imagepath,"rb")
	    self.wfile.write(pngfile.read())
	    pngfile.close()
        elif imagepath.endswith(".gif"):
	    self.send_response(200)
	    self.send_header("Content-type","image/gif")
	    self.end_headers()	
	    giffile = open(imagepath,"rb")
	    self.wfile.write(giffile.read())
	    giffile.close()

	else:
	    self.send_response(404)


    def download_fractal_param_dat(self):
        self.send_response(200)
        self.send_header("Content-type","application/x-download")
        self.send_header("Content-disposition","attachement; filename='filenametest'")
        self.end_headers()
        
        fractal_para=self.imageAdministrator.get_parameters()
        fractal_para_str=repr(fractal_para)

        self.wfile.write(fractal_para_str)


    def get_new_coordinate(self,querydict):
	"""
	extract new center of image after the user click out of the url
	"""	
	number = re.compile(r"([0-9]+)")
	if number.match(querydict["zoom_offset.x"][0]) is None or number.match(querydict["zoom_offset.y"][0]) is None:
	    self.send_response(400, "offset out of range")
	#TODO what happens after a 400?    
	else:
	    new_x = int(querydict["zoom_offset.x"][0])
	    new_y = int(querydict["zoom_offset.y"][0])
	    """
	regExp = re.compile(r"x=([0-9]+)")
	new_x= string.atoi(regExp.findall(self.path)[0])
	regExp = re.compile(r"y=([0-9]+)")
	new_y = string.atoi(regExp.findall(self.path)[0]) 
	    """
	return new_x, new_y
 
	
	
if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    #piggybacking imageadministrator into Myhandler instead of using it globally
    #idea: this could be a singleton pattern    
    httpd.colorAlg = coloralg.ColorAlg()
    httpd.imageAdministrator = imageAdministrator.ImageAdministrator(httpd.colorAlg)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

