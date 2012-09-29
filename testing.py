import ImageDraw,Image

#testing catmullrom with continuos values
#TODO test all coloring algorithm combinations 
def test_catmullrom(colorAlg,colorscheme):

    imagewidth = 400
    imageheight = 50
    image = Image.new("RGB",(imagewidth, imageheight))
    draw = ImageDraw.Draw(image)

    points = range(imagewidth)
    for point in points:
	points[point] = float(point)/imagewidth*len(colorscheme)

    for x in range(imagewidth):
	assignedcolor = colorAlg.catmullrom(points[x])
	formattedcolor = "#"+assignedcolor
	for y in range(imageheight):
	    draw.point((x,y),fill=formattedcolor)

    image.show()    

def test_straightconnection(colorAlg,colorscheme):

    imagewidth = 400
    imageheight = 50
    image = Image.new("RGB",(imagewidth, imageheight))
    draw = ImageDraw.Draw(image)

    points = range(imagewidth)
    for point in points:
	points[point] = float(point)/imagewidth*len(colorscheme)

    for x in range(imagewidth):
	assignedcolor = colorAlg.straightconnection((points[x],len(colorscheme)))
	formattedcolor = "#"+assignedcolor
	for y in range(imageheight):
	    draw.point((x,y),fill=formattedcolor)

    image.show()    


class Test_Minmaxvalue():

    def __init__(self,maxiteration):

        self.z_maxvalue = [0.0 for x in range(maxiteration+1)]
        self.z_minvalue = [10000.0 for x in range(maxiteration+1)]

        self.p_maxvalue = [0.0 for x in range(maxiteration+1)]
        self.p_minvalue = [10000.0 for x in range(maxiteration+1)]
    def record_minmax(self,colorAlg,iteration,z):
        (p_value,t) = colorAlg.distanceestimator4(iteration,z)
        z_value = abs(z)

        if p_value > self.p_maxvalue[iteration]:
            self.p_maxvalue[iteration] = p_value
        elif p_value < self.p_minvalue[iteration]:
            self.p_minvalue[iteration] = p_value
        else:
            pass

        if z_value > self.z_maxvalue[iteration]:
            self.z_maxvalue[iteration] = z_value
        elif z_value < self.z_minvalue[iteration]:
            self.z_minvalue[iteration] = z_value
        else:
            pass


    def print_minmax(self):

        print "p minima"
        print self.p_minvalue

        print "p maxima"
        print self.p_maxvalue


        print "z minima"
        print self.z_minvalue

        print "z maxima"
        print self.z_maxvalue


    
