import math
from PIL import Image, ImageDraw, ImageFilter
# import testing
#TODO possible separation of saving and calculating the image, formatting input variables, adjust variablenames, how everything works together

def calculate_mandelbrot(   colorAlg,
                            imageheight=600,
			    imagewidth=600,
			    maxiteration=10,
                            xabsolutestart= -2.0,
                            xabsoluteend=2.0,
                            yabsolutestart=-2.0,
                            yabsoluteend=2.0,
                            colorscheme=["000000","338822","883388"],
                            saveFileName="images/Mandelbrot.png"):
    """ 
    generates a mandelbrot fractal image and is saved as .png

    Arguments:
        colorAlg:       choice of a coloring algorithm and the colorschemes
        imageheight,
        imagewidth:     pixelsize of the image to be calculated
        maxiteration:   directly correlated to the duration of the calculation
        absolutestart, 
        absoluteend:    the cornerpoints of the section of the image to be calculated
                        in the complex plane 
        colorscheme:    the cornerpoints of the continous, colorscheme
                        minimum number of elements should be 3, the first color
                        depicts the nonescaping pixels(default = black) 
                        input according to ImageDraw as hexstring 
                        for example "#D3D3D3"
        saveFileName:   image is saved under that name and location
    """
    #test_minmax = testing.Test_Minmaxvalue(maxiteration)
    print "calculating mandelbrot"
    print locals()
    
    # create new image file
    image = Image.new("RGB", (imagewidth,imageheight))
    draw = ImageDraw.Draw(image)

    # iterate over all the points in the image
    escapelimit = 2	#mathematical escapelimit = 2, though other values can be chosen
    iteration =0
    xCoord = range(imagewidth)
    yCoord = range(imageheight)
    # TODO replace with matrix multiplication 
    for x in xCoord:
        for y in yCoord:
	    iteration =0

            #convert [x,y] in range [0,imagesize] to complex z0 in range [absolutestart, absoluteend]
            z0x = xabsolutestart+(xabsoluteend-xabsolutestart)/imagewidth*x
            z0y = yabsolutestart+(yabsoluteend-yabsolutestart)/imageheight*y
            z0 = complex(z0x,z0y)

            #apply equation
    	    z = complex(0,0)	
    	    while (iteration < maxiteration and  abs(z) < escapelimit):
                prevz = z
    	        z = z**2 + z0
    	        iteration = iteration + 1
            #test_minmax.record_minmax(colorAlg, iteration,z)

    	    #assign color to current point
    	    if iteration == (maxiteration):
    	        assignedcolor = colorscheme[0]
    	    else:
                assignedcolor = colorAlg.straightconnection(colorAlg.distanceestimator1(iteration,z,prevz,escapelimit))
            #assignedcolor = colorAlg.straightconnection(colorAlg.calculateangle(iteration,z))

	    #convert to "#FF03CD" as required by the ImageDraw library
	    formattedcolor = "#"+assignedcolor
    	    draw.point((x,y),fill=formattedcolor)
    
    # save picture            
    image.save(saveFileName,"PNG")
    
    #test_minmax.print_minmax()
