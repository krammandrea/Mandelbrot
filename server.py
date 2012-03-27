"""Interprets the user clicks on the website and relates the parameter to the Mandelbrot calculating class
"""
import string
import re
import BaseHTTPServer
import mandelbrot
import math

HOST_NAME = '' # empty because using http://localhost
PORT_NUMBER = 8080

#TODO: put class in new file, find name, find the big picture, comment pydoc, comment variables, is it a module?
class ImageAdministrator():
    """stores the current parameters of the image which the user changes until he is satisfied and saves the image and the accompaning calculating data to file""" 
    GREEN =["#000000","#336633","#33664D","#336666","#334D66","#333366","#4D3366","#663366","#66334D","#663333","#664D33","#666633","#4D6633"]
    BROWNBLUE = ["#000000","#FF9900","#BF8630","#A66300","#FFB240","#FFC773","#689CD2","#4188D2","#04376C","#26517C","#0D58A6"]
    #"""default colorscheme in brown and blue"""
    def __init__(self):
	self.height = 600
	self.width = 600
	self.maxiteration = 20
        self.xabsolutestart = -2.0
        self.xabsoluteend = 2.0
        self.yabsolutestart = -2.0
        self.yabsoluteend = 2.0
	self.colorscheme = self.BROWNBLUE	


    def change_imagesize(self,new_width, new_height):
#TODO remember to adjust zoomfactor if zoom=1 and image not quadratic
        """adjust dependent offsetabsolute"""
        #adjust the new x/yabsolutestart/end to the new aspectratio, so the detail of the image has still the same surface and is centered around the old centerpoint
        new_ratio = float(new_height)/float(new_width)
        surface = (self.xabsoluteend-self.xabsolutestart)*(self.yabsoluteend-self.yabsolutestart)
        new_xabsolutewidth = math.sqrt(surface/new_ratio)
        new_yabsoluteheight = math.sqrt(surface*new_ratio)
        width_difference = new_xabsolutewidth-(self.xabsoluteend-self.xabsolutestart)
        height_difference = new_yabsoluteheight-(self.yabsoluteend-self.yabsolutestart)
        self.xabsolutestart -= 0.5*width_difference
        self.xabsoluteend   += 0.5*width_difference
        self.yabsolutestart -= 0.5*height_difference
        self.yabsoluteend   += 0.5*height_difference
        self.height = new_height
        self.width  = new_width
#TODO

    def reset_to_default(self):
	pass


    def change_zoom(self,zoom_relative):
        #zoom = 1 original image
        #zoom = 2 halfs the section of the image 
        newimagewidth   = (self.xabsoluteend-self.xabsolutestart)/zoom_relative
        newimageheight  = (self.yabsoluteend-self.yabsolutestart)/zoom_relative 
        oldimagewidth   = (self.xabsoluteend-self.xabsolutestart)
        oldimageheight  = (self.yabsoluteend-self.yabsolutestart)
        self.xabsolutestart += 0.5*(oldimagewidth-newimagewidth) 
        self.xabsoluteend   -= 0.5*(oldimagewidth-newimagewidth)
        self.yabsolutestart += 0.5*(oldimageheight-newimageheight)
        self.yabsoluteend   -= 0.5*(oldimageheight-newimageheight)     

    def change_offset(self, xoffsetfactor, yoffsetfactor):
        xabsoluteoffset = xoffsetfactor*(self.xabsoluteend - self.xabsolutestart) 
        yabsoluteoffset = yoffsetfactor*(self.yabsoluteend - self.yabsolutestart) 

	self.xabsolutestart += xabsoluteoffset
	self.yabsolutestart += yabsoluteoffset
        self.xabsoluteend += xabsoluteoffset
        self.yabsoluteend += yabsoluteoffset       


    def change_offset_and_zoom(self, new_center_x, new_center_y,zoom_on_click):
        #calculate offset in the pixelcoordinates then transform to the absolute complex plane and calculate the new cornerpoints    
        xabsoluteoffset = (new_center_x - self.width/2)*(self.xabsoluteend - self.xabsolutestart)/self.width
        yabsoluteoffset = (new_center_y - self.height/2)*(self.yabsoluteend - self.yabsolutestart)/self.height

	self.xabsolutestart += xabsoluteoffset
	self.yabsolutestart += yabsoluteoffset
        self.xabsoluteend += xabsoluteoffset
        self.yabsoluteend += yabsoluteoffset       

        #the zoom_on_click reduces the original size while the center stays the same
        self.change_zoom(zoom_on_click)


    def change_colorscheme(self,new_colorscheme):
        self.colorscheme = new_colorscheme


    def change_maxiteration(self,new_iteration):
	self.maxiteration = new_iteration

    def get_parameters(self):
	return self.height, self.width, self.maxiteration, self.xabsolutestart, self.xabsoluteend, self.yabsolutestart, self.yabsoluteend, self.colorscheme
    def save_parameters_to_file(self):
	pass


#TODO rename file, restructre if/else part and add comments what the user actions are 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    ZOOM_ON_CLICK= 2.0
    OFFSETFACTOR = 0.20 #image section moves by 20%    
    ZOOMRELATIVE = 2.0    
        

    def __init__(self,request, client_adress,server):
        self.imageAdministrator = server.imageAdministrator
        BaseHTTPServer.BaseHTTPRequestHandler.__init__(self,request,client_adress,server)


#TODO hash table for url path instead of if elif
    def do_GET(self):
	if self.path.endswith("index.html"):
	    mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
	    self.do_GET_main_page()
	elif self.path.endswith("/"):
	    mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
	    self.get_main_page()
	elif self.path.find("/images/") >=0:
            pathname = self.path.partition("images/")[1]+self.path.partition("images/")[2]
            self.get_image(pathname)
        elif self.path.find("/style/")>=0:
            self.get_css(self.path.rpartition("style/")[-1])
        elif self.path.find("change_color") >=0:
            new_colors = self.get_colors(self.path.partition("change_color")[2])
            self.imageAdministrator.change_colorscheme(new_colors)
	    mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
            self.get_main_page()
        elif self.path.find("iteration")>=0:
            new_iteration = self.get_iteration(self.path.partition("iteration")[2])
            self.imageAdministrator.change_maxiteration(new_iteration)
	    mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
            self.get_main_page()
        elif self.path.find("change_size")>=0:
            new_width,new_height = self.get_size(self.path.partition("change_size")[2])
            self.imageAdministrator.change_imagesize(new_width,new_height)
	    mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
            self.get_main_page()
        elif "/javascript"in self.path and ".js"in self.path:
            pathname = self.path.partition("javascript/")[1]+self.path.partition("javascript/")[2]
            self.get_jscolor(pathname)
        elif("javascript/"in self.path and(".png" in self.path or ".gif" in self.path)):
            pathname = self.path.partition("javascript/")[1]+self.path.partition("javascript/")[2]
            self.get_image(pathname)
	elif 'zoom_offset' in self.path:
	    """when clicking into the image the new image will be calculated centered around the clicked point"""
	    new_x,new_y = self.get_new_coordinate()
	    self.imageAdministrator.change_offset_and_zoom(new_x,new_y,self.ZOOM_ON_CLICK)
	    mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())	
	    self.get_main_page()   
            """when clicking on arrow buttons the new image section will move to the corresponding direction"""
        elif 'offset_right' in self.path:
            self.imageAdministrator.change_offset(self.OFFSETFACTOR,0)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 
        elif 'offset_left' in self.path:
            self.imageAdministrator.change_offset(-self.OFFSETFACTOR,0)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 
        elif 'offset_up' in self.path:
            self.imageAdministrator.change_offset(0,-self.OFFSETFACTOR)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 
        elif 'offset_down' in self.path:
            self.imageAdministrator.change_offset(0,self.OFFSETFACTOR)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 
        elif 'zoom_in' in self.path:
            self.imageAdministrator.change_zoom(self.ZOOMRELATIVE)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 
        elif 'zoom_out' in self.path:
            self.imageAdministrator.change_zoom(1/self.ZOOMRELATIVE)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 
        elif 'zoom' in self.path:
            self.imageAdministrator.change_zoom(self.ZOOMRELATIVE)
            mandelbrot.calculate_mandelbrot(*self.imageAdministrator.get_parameters())
            self.get_main_page() 
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

    def get_css(self,cssname):
        if cssname.endswith(".css"):
            self.send_response(200)
            self.send_header("Content-type","text/css")
            self.end_headers()
            cssfile = open(cssname,"rb")
            self.wfile.write(cssfile.read())
            cssfile.close()            
        else:
            self.send_response(404)    

    def get_size(self,sizestring):
	regExp = re.compile(r"height=([0-9]+)")
	new_height= string.atoi(regExp.findall(self.path)[0])
	regExp = re.compile(r"width=([0-9]+)")
	new_width= string.atoi(regExp.findall(self.path)[0])
        return new_width,new_height


    def get_jscolor(self,jscolorpath):
        if jscolorpath.endswith("jscolor.js"):
            self.send_response(200)
            self.send_header("Content-type","text/js")
            self.end_headers()
            jscolorfile = open(jscolorpath,"rb")
            self.wfile.write(jscolorfile.read())
            jscolorfile.close()
        else:
            self.send_response(404)        

    def get_colors(self,colorstring):
        #find all the hex numbers in between "col=" and  "&"

        regExp = re.compile("([0-9a-fA-F]+)(?=&)")
	new_colors = regExp.findall(self.path)
        #filter out bad results

        #add "#" in string as required by the ImageDraw library
        new_colors_formatted = ['#'+ color for color in new_colors]
        return new_colors_formatted
    
    def get_iteration(self,iterationstring):
        regExp = re.compile("[0-9]{1,2}")
        new_iteration = string.atoi(regExp.findall(iterationstring)[0]) 
        print new_iteration
        return new_iteration

#TODO else only after imagename not existent 
    def get_image(self,imagepathname):
    #responds to a request for an image by checking for the file in folder /images	
	if imagepathname.endswith(".png"):
	    self.send_response(200)
	    self.send_header("Content-type","image/png")
	    self.end_headers()	
	    pngfile = open(imagepathname,"rb")
	    self.wfile.write(pngfile.read())
	    pngfile.close()
        elif imagepathname.endswith(".gif"):
	    self.send_response(200)
	    self.send_header("Content-type","image/gif")
	    self.end_headers()	
	    giffile = open(imagepathname,"rb")
	    self.wfile.write(giffile.read())
	    giffile.close()

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

