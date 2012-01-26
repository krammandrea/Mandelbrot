import Image, ImageDraw
#TODO pydoc commentary, possible separation of saving and calculating the image, formatting input variables, adjust variablenames, how everything works together
#TODO calculate the absolute zoom from the relative zoom, see what the zoomnumbers do? range? experiment with the zoomfactor, divide through imagewidth/length really necessary?experiment!


""" pydoc

"""
def calculate_mandelbrot(imageheight=400,
                         imagewidth=400,
                         maxiteration=10,
                         offsetx=0,
                         offsety=0,
                         zoomfactor=1,
                         colorscheme=[(0,0,0),(51,102,51),(51,102,77),(51,102,102),(51,77,102),(51,51,102),(77,51,102),(102,51,102),(102,51,77),(102,51,51),(102,77,51),(102,102,51),(77,102,51)]):
        #imageheight,imagewidth: pixelsize of the image
        #maxiteration: directly correlated to the duration of the calculation ?when does it get too long
        #offsetx, offsety: absolute new center of the reference image
        #zoomfactor: absolute zoomfactor range 1 to indefinitely
        #colorscheme: 12 elements, default value is green

#TODO adjust   zoomfactor = 0.9
    xCoord = range(imagewidth)
    yCoord = range(imageheight)
    # define used colors
    #GREEN = [(0,0,0),(51,102,51),(51,102,77),(51,102,102),(51,77,102),(51,51,102),(77,51,102),(102,51,102),(102,51,77),(102,51,51),(102,77,51),(102,102,51),(77,102,51)]
    #RED = [(0,0,0),(255,0,0),(255,128,0),(255,255,0),(128,255,0),(0,255,0),(0,255,128),(0,255,255),(0,128,255),(0,0,255),(128,0,255),(255,0,255),(255,0,128)]
    
    # create new image file
    iteration =0
    image = Image.new("RGB", (imagewidth,imageheight))
    draw = ImageDraw.Draw(image)
    # iterate over all the points in the image
    for x in xCoord:
        for y in yCoord:
	   iteration =0
	    #mitte vom bild am geklickten Punkt
	    #moves the image to the new centerpoint and stretches to accomodate to the pixelsize and the absolute zoomfactor
	    #absolute size of Mandelbrot is 4 times 4
    	   z0 = complex(4*(float(x)-imagewidth/2-offsetx)/imagewidth/zoomfactor,4*(float(y)-imageheight/2-offsety)/imageheight/zoomfactor)
    	   z = complex(0,0)	#z=0+0*j
    	   #apply equation
    	   while (iteration < maxiteration and  abs(z*z.conjugate()) < 3**2):
    	       z = z**2 + z0
    	       iteration = iteration + 1
    	   #assign color to current point
    	   if iteration == (maxiteration):
    	       assignedcolor = colorscheme[0]
    	   else:
    	       assignedcolor = colorscheme[iteration%12+1]
    	   draw.point((x,y),fill=assignedcolor)
    
    # save picture
    image.save("MandelbrotImg/Mandelbrot.png","PNG")
    
    # show picture
    # image.show()
