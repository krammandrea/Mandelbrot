import math,testing

class ColorAlg():
 
    def __init__(self, colorscheme = ["000000","338822","883388"]):	
	"""
        initializes algorithms in advance for faster computing time
        """

	self.initcolorscheme(colorscheme)
	

    def initcolorscheme(self,colorscheme):
	"""
	converts 
	"""
	#convert the colorscheme from list of strings to rgb matrix
	self.colorscheme = [[0.0 for x in range(3)] for y in range(len(colorscheme))]
	for color in range(len(colorscheme)):
	    intcolor = int(colorscheme[color],16)
	    #convert to rgb in range [0,255]
	    self.colorscheme[color][0] =    float((intcolor&0xff0000)>>16)
	    self.colorscheme[color][1] =    float((intcolor&0x00ff00)>>8)
	    self.colorscheme[color][2] =    float((intcolor&0x0000ff)>>0)
    
	self.initcatmullrom()

        #show the current colorscheme
        testing.test_catmullrom(self,colorscheme)
        testing.test_straightconnection(self,colorscheme)

    def initcatmullrom(self):
        """
        precalculate all possible matrixes [P(i-1),P(i),P(i+1),P(i+2)]*Mcr for 
        the current colorscheme
        """
	self.PtimesMcr = [[[0.0 for x in range(4)]for y in range(3)] for z in range(len(self.colorscheme))]
        tau = 0.5   #curve sharpness of the spline
        Mcr =[[0.0,-1.0*tau,2.0*tau,-1.0*tau],[2.0*tau,0.0,-5.0*tau,3.0*tau],[0.0,1.0*tau,4.0*tau,-3.0*tau],[0.0,0.0,-1.0*tau,1.0*tau]]    
	for x in range(len(self.colorscheme)):
	    P = [self.colorscheme[-1+x],self.colorscheme[x],self.colorscheme[(x+1)%len(self.colorscheme)],self.colorscheme[(x+2)%len(self.colorscheme)]]
	    for y in range(len(P[0])):
		for z in range(len(Mcr[0])):
		    self.PtimesMcr[x][y][z] = sum(list(P[j][y] * Mcr[j][z] for j in range(len(P)) ))
  
                  
    def escapetime(self,iteration,z):
	"""
        coloring represents the number of iterations before z escapes
        """
        colorIndikator = iteration

        return (colorIndikator, len(self.colorscheme))  

    def calculateangle(self,iteration, z):
        """
        coloring represents the angle of the escaped z
        """
        angle = math.asin(z.real/abs(z))
        colorIndikator = angle

        return (colorIndikator, 2*math.pi)

    def distanceestimator1(self, iteration, z,prevz,escapelimit):
        """normalized iteration count, details in http://math.unipa.it/~grim/Jbarrallo.PDF
        """
	colorIndikator = iteration + 1 - ((math.log10(math.log10(abs(z))))/math.log10(2))

	return (colorIndikator, len(self.colorscheme))

   
    def distanceestimator2(self, iteration, z):
        """
        continuous potential algorithm, see http://math.unipa.it/~grim/Jbarrallo.PDF
        """
        colorIndikator = math.log10(abs(z))/(2**math.log10(iteration))

        return (colorIndikator, len(self.colorscheme))


    def distanceestimator3(self, iteration, z):
        """
        distance estimation algorithm, see http://math.unipa.it/~grim/Jbarrallo.PDF
        """
        colorIndikator = 2*math.log10(abs(z))
        
        return (colorIndikator, len(self.colorscheme))

    def distanceestimator4(self, iteration, z):
        """
        e to the power of (-|z|) smoothing, see http://math.unipa.it/~grim/Jbarrallo.PDF
        """
        colorIndikator = math.exp(-(abs(z)))

        return (colorIndikator,0.13)
        
    def distanceestimator5(self, iteration, z, escapelimit):
        """
        coloring represents the distance to the escapelimit
        """
        colorIndikator = abs(z) - escapelimit
        return (colorIndikator, 3.0)

    def distanceestimator6(self,iteration, z, prevz, escapelimit):
        """
        matthias algorithm, coloring represents the number of iterations plus the 
        percentage of the distance to the escapelimit
        """
        colorIndikator =iteration + 1 - (abs(z)-escapelimit)/(abs(z)-abs(prevz))

        return (colorIndikator, len(self.colorscheme))


    def catmullrom(self, colorIndikator):
        #TODO
        """
        creates the colorscheme(size:1000) using the given cornerpoints and 
        connecting them with catmullrom splines
        p(s) = [P(i-1),P(i),P(i+1),P(i+2)]*M(cr)*[1 t^2 t^3 t^4]
        """
	assignedcolor = [0.0 for rgb in range(3)]

	#choose the precalculated matrix [P(i-1),P(i),P(i+1),P(i+2)]M(cr) for the current section, which the color is roughly in
	currentcolor = int(colorIndikator%len(self.colorscheme))    	
	partial_colInd = colorIndikator%1 #using %1 causes minor rounding errors

	Tvector = [1, partial_colInd**2, partial_colInd**3, partial_colInd**4]	
        
        #allowed range for Tvector [0,1]
	for rgb in range(3):
	    assignedcolor[rgb] = sum(self.PtimesMcr[currentcolor][rgb][j] * Tvector[j] for j in range(4))
		
	return self.convertToString(assignedcolor)


    def clampoff(self,(colorIndikator,normalizdTo)):
        #TODO use colorscheme once and assigned maximum values to any over the border value
        #TODO find a way to integrate this into the distanceestimators 
    
        pass


    def straightconnection(self, (colorIndikator, normalizedTo)):
        #TODO
        """
        creates the colorscheme using the given cornerpoints and connecting them
        with straight lines
        """
    #cornerpoints of the colorscheme connected with straight lines 

	assignedcolor = [0.0 for rgb in range(3)]
        #currentcolor = int(colorIndikator%len(self.colorscheme))
        #partial_colInd = colorIndikator%1
	
        #within a picked random normalizedTo-Value the colorscheme repeats itself once
        #cut off so only values in between 0 and normalizedTo
        cutoff= colorIndikator%(normalizedTo)
        #find out in which area of the colorscheme(currentcolor) and how far into it(rest) the current value is 
        rest = cutoff%(normalizedTo/float(len(self.colorscheme)))
        currentcolor = int((cutoff-rest)/(normalizedTo/float(len(self.colorscheme))))   #convert to int to catch rounding errors
        #stretch the rest to range [0,1] 
        partial_colInd = rest * float(len(self.colorscheme))/normalizedTo 
	for rgb in range(3):
	    assignedcolor[rgb] = self.colorscheme[currentcolor][rgb] + (self.colorscheme[(currentcolor+1)%len(self.colorscheme)][rgb] - self.colorscheme[currentcolor][rgb]) * partial_colInd

	return self.convertToString(assignedcolor)    


    def convertToString(self,rgbFloatColor):
        """
        converts a RGB color from float to int, while checking for out of bound values
           [0,255], then to a hexadezimal string
        """
	intcolor = [0 for x in range(3)]
	for color in range(len(rgbFloatColor)):
	    intcolor[color] = int(rgbFloatColor[color])
	    if intcolor[color]<0:
		intcolor[color] = 0
	    elif intcolor[color]>255:
		intcolor[color] = 255
	    else:
		pass
	
	#combine to one hexnumber and convert to string in the '02DE3F'format
	hexStringColor = '{:02X}{:02X}{:02X}'.format(*intcolor)
	return hexStringColor

	

