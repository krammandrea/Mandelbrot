import math, coloralg
#TODO: put class in new file, find name, find the big picture, comment pydoc, comment variables, is it a module?
class ImageAdministrator():
    """
    stores the current parameters of the image which the user changes until he is 
    satisfied and saves the image and the accompaning calculating data to file
    """ 
    
    GREEN =["000000","336633","33664D","336666","334D66","333366","4D3366","663366","66334D","663333","664D33","666633","4D6633"]
    BROWNBLUE = ["000000","FF9900","BF8630","A66300","FFB240","FFC773","689CD2","4188D2","04376C","26517C","0D58A6"]
    PURPLEGREEN = ["55285E","4B2B52","451A4E","7B4686","7C4E86","A1A95F","A0A956","6B7326","747A3E","838C3D"]


    def __init__(self, colorAlg):
	self.height = 600
	self.width = 600
	self.maxiteration = 20
        self.xabsolutestart = -2.5
        self.xabsoluteend = 1.5
        self.yabsolutestart = -2.0
        self.yabsoluteend = 2.0
	self.colorscheme = self.PURPLEGREEN	
	self.coloralg = colorAlg
        colorAlg.__init__(self.colorscheme[1:len(self.colorscheme)])
        print "initaliazing imageAdministrator"

    def change_imagesize(self,new_width, new_height):
        """
        adjust the pixelsize of the image and adjust the new x/yabsolutestart/end 
        to the new aspectratio, so the detail of the image has still the same surface 
        and is centered around the old centerpoint
        """
        #TODO catch out of bounds
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


    def change_section(self,new_borderlines):
        """
        change to section of the image keeping the width constant and adjusting the 
        height to the new ratio 
        """
        #TODO catch out of bounds
        self.xabsolutestart = new_borderlines[0]
        self.xabsoluteend   = new_borderlines[1]
        self.yabsolutestart = new_borderlines[2]
        self.yabsoluteend   = new_borderlines[3]
        
        new_ratio  = (self.yabsoluteend - self.yabsolutestart)/(self.xabsoluteend - self.xabsolutestart)
        
        self.height = int(self.width * new_ratio)

    def change_zoom(self,zoom_relative):
        """
        zoom into the picture with zoom=1 showing the orginal section and 
        zoom=2 half the section shown
        """
        #TODO catch out of bounds
        newimagewidth   = (self.xabsoluteend-self.xabsolutestart)/zoom_relative
        newimageheight  = (self.yabsoluteend-self.yabsolutestart)/zoom_relative 
        oldimagewidth   = (self.xabsoluteend-self.xabsolutestart)
        oldimageheight  = (self.yabsoluteend-self.yabsolutestart)

        self.xabsolutestart += 0.5*(oldimagewidth-newimagewidth) 
        self.xabsoluteend   -= 0.5*(oldimagewidth-newimagewidth)
        self.yabsolutestart += 0.5*(oldimageheight-newimageheight)
        self.yabsoluteend   -= 0.5*(oldimageheight-newimageheight)     


    def change_offset(self, xoffsetfactor, yoffsetfactor):
        """
        move the section of the image by the given percentage of the imagesize, 
        default is 20%, range is [0,1.0]
        """
        xabsoluteoffset = xoffsetfactor*(self.xabsoluteend - self.xabsolutestart) 
        yabsoluteoffset = yoffsetfactor*(self.yabsoluteend - self.yabsolutestart) 

	self.xabsolutestart += xabsoluteoffset
	self.yabsolutestart += yabsoluteoffset
        self.xabsoluteend += xabsoluteoffset
        self.yabsoluteend += yabsoluteoffset       


    def change_offset_and_zoom(self, new_center_x, new_center_y,zoom_on_click):
        """
        calculate offset in the pixelcoordinates then transform to the absolute 
        complex plane and calculate the new cornerpoints
        zoom_on_click reduces the original size while the center stays the same
        """ 
        xabsoluteoffset = (new_center_x - self.width/2)*(self.xabsoluteend - self.xabsolutestart)/self.width
        yabsoluteoffset = (new_center_y - self.height/2)*(self.yabsoluteend - self.yabsolutestart)/self.height

	self.xabsolutestart += xabsoluteoffset
	self.yabsolutestart += yabsoluteoffset
        self.xabsoluteend += xabsoluteoffset
        self.yabsoluteend += yabsoluteoffset       

        self.change_zoom(zoom_on_click)


    def change_colorscheme(self,new_colorscheme):
        """
        change the colorscheme, minimum number of colors is 3
        """
        #TODO minimum number of colors
        self.colorscheme = new_colorscheme
        print self.colorscheme, new_colorscheme

    def change_maxiteration(self,new_iteration):
        """
        change the number of maximum interations, a higher number gives a more detailed
        picture
        """
	self.maxiteration = new_iteration


    def get_parameters(self):
	return self.coloralg, self.height, self.width, self.maxiteration, self.xabsolutestart, self.xabsoluteend, self.yabsolutestart, self.yabsoluteend, self.colorscheme
        

    def save_parameters_to_file(self):
	pass
