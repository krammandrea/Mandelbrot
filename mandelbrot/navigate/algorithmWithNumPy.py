import math
import numpy
from PIL import Image, ImageDraw, ImageFilter
# import testing
#TODO possible separation of saving and calculating the image, formatting input variables, adjust variablenames, how everything works together

def calculate_mandelbrot(   
                            imageheight=1000,
                            imagewidth=1000,
                            maxiteration=40,
                            xabsolutestart= -2.0,
                            xabsoluteend=2.0,
                            yabsolutestart=-2.0,
                            yabsoluteend=2.0,
                            colorscheme=[{"red": 0, "green":0, "blue":0},
                                        {"red": 33, "green":88, "blue":22},
                                        {"red": 88, "green":33, "blue":88}],
                            saveFileName="/Users/Work/Desktop/Mandelbrot.png"):
                            # colorAlg,
                            # colorscheme=["000000","338822","883388"],
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
    print "calculating mandelbrot"
    
    # iterate over all the points in the image
    escapelimit = 2 #mathematical escapelimit = 2, though other values can be chosen
    iteration =0
    xCoord = range(imagewidth)
    yCoord = range(imageheight)

    import numpy as np
    # generate matrix Z with range imagewidth, imageheight
    Z = numpy.zeros((imagewidth,imageheight),dtype=complex)

    # Initialize matrix showing the x/y coordinate as the value
    numpy.array(range(imagewidth))
    XPosition = numpy.reshape(numpy.repeat(numpy.array(range(imageheight)),imagewidth), newshape=[imageheight, imagewidth]).transpose()
    YPosition = numpy.reshape(numpy.repeat(numpy.array(range(imagewidth)),imageheight), newshape=[imagewidth, imageheight])

    # Convert to complex coordinate system in the desired range [absolutestart, absoluteend]
    XCoord = xabsolutestart+(xabsoluteend-xabsolutestart)/imagewidth * XPosition
    YCoord = yabsolutestart+(yabsoluteend-yabsolutestart)/imageheight* YPosition

    Z0 = XCoord + complex(0,1) * YCoord

    IterBeforeEscape = numpy.zeros((imagewidth,imageheight), dtype=int)
    # initialize resultIteration zeros imagewidth, imageheight 

    iteration = 0
    while (iteration < maxiteration):
        # Where abs(Z) is smaller then the escapelimit, calculate new value, otherwise keep previous value
        Z = numpy.where(abs(Z)<escapelimit, Z*Z+Z0, Z)
        iteration += 1
        # Remember number of iterations before escapelimit is hit
        IterBeforeEscape = numpy.where(abs(Z)<escapelimit, iteration, IterBeforeEscape)

    # Assign color
    IterBeforeEscape = IterBeforeEscape % maxiteration # convert all maxiteration values to 0 
    IterBeforeEscape = IterBeforeEscape % len(colorscheme)  # repeat colors 
    AssignedColor = numpy.zeros((imagewidth, imageheight, 3), dtype='uint8')

    for ind, color in enumerate(colorscheme):
        AssignedColor[...,0] = numpy.where(IterBeforeEscape==ind, colorscheme[ind]["red"], AssignedColor[...,0])
        AssignedColor[...,1] = numpy.where(IterBeforeEscape==ind, colorscheme[ind]["green"], AssignedColor[...,1])
        AssignedColor[...,2] = numpy.where(IterBeforeEscape==ind, colorscheme[ind]["blue"], AssignedColor[...,2])

    img = Image.fromarray(AssignedColor)
    img.save(saveFileName, "PNG")




    # # TODO replace with matrix multiplication 
    # for x in xCoord:
    #     for y in yCoord:
    #     iteration =0

    #         #convert [x,y] in range [0,imagesize] to complex z0 in range [absolutestart, absoluteend]
    #         z0x = xabsolutestart+(xabsoluteend-xabsolutestart)/imagewidth*x
    #         z0y = yabsolutestart+(yabsoluteend-yabsolutestart)/imageheight*y
    #         z0 = complex(z0x,z0y)

    #         #apply equation
    #         z = complex(0,0)    
    #         while (iteration < maxiteration and  abs(z) < escapelimit):
    #             prevz = z
    #             z = z**2 + z0
    #             iteration = iteration + 1
    #         #test_minmax.record_minmax(colorAlg, iteration,z)

    #         #assign color to current point
    #         if iteration == (maxiteration):
    #             assignedcolor = colorscheme[0]
    #         else:
    #             assignedcolor = colorAlg.straightconnection(colorAlg.distanceestimator1(iteration,z,prevz,escapelimit))
    #         #assignedcolor = colorAlg.straightconnection(colorAlg.calculateangle(iteration,z))

    #     #convert to "#FF03CD" as required by the ImageDraw library
    #     formattedcolor = "#"+assignedcolor
    #         draw.point((x,y),fill=formattedcolor)
    
    # # save picture            
    # image.save(saveFileName,"PNG")
    
    #test_minmax.print_minmax()
