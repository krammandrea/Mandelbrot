import Image, ImageDraw
#TODO pydoc commentary, possible separation of saving and calculating the image, formatting input variables, adjust variablenames, how everything works together
#TODO calculate the absolute zoom from the relative zoom, see what the zoomnumbers do? range? experiment with the zoomfactor, divide through imagewidth/length really necessary?experiment!


""" pydoc

"""
def calculate_mandelbrot(imageheight=400,
                         imagewidth=400,
                         maxiteration=10,
                            xabsolutestart= -2.0,
                            xabsoluteend=2.0,
                            yabsolutestart=-2.0,
                            yabsoluteend=2.0,
                         colorscheme=[(0,0,0),(51,102,51),(51,102,77),(51,102,102),(51,77,102),(51,51,102),(77,51,102),(102,51,102),(102,51,77),(102,51,51),(102,77,51),(102,102,51),(77,102,51)]):
        #imageheight,imagewidth: pixelsize of the image
        #maxiteration: directly correlated to the duration of the calculation ?when does it get too long
        #absolutestart, absoluteend: the coordinates of the section of the image to be calculated  
        #colorscheme: 12 elements, default value is green
    print xabsolutestart,xabsoluteend

    xCoord = range(imagewidth)
    yCoord = range(imageheight)
    #possible color schemes
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
            
            #convert [x,y] in range [0,imagesize] to complex z0 in range [absolutestart, absoluteend]
                
            z0x = xabsolutestart+(xabsoluteend-xabsolutestart)/imagewidth*x
        
            z0y = yabsolutestart+(yabsoluteend-yabsolutestart)/imageheight*y
            z0 = complex(z0x,z0y)

            #apply equation
    	    z = complex(0,0)	#z=0+0*j
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
    image.save("images/Mandelbrot.png","PNG")
    
    # show picture
    # image.show()
