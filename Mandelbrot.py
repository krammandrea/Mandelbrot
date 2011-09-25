import Image, ImageDraw


# define image size
imagesize = 1000
maxiteration = 30
xCoord = range(imagesize)
yCoord = range(imagesize)
zoom = 1.1
offsetx= 7500
offsety= 5000
# define used colorsi
GREEN = [(0,0,0),(51,102,51),(51,102,77),(51,102,102),(51,77,102),(51,51,102),(77,51,102),(102,51,102),(102,51,77),(102,51,51),(102,77,51),(102,102,51),(77,102,51)]
RED = [(255,0,0),(255,128,0),(255,255,0),(128,255,0),(0,255,0),(0,255,128),(0,255,255),(0,128,255),(0,0,255),(128,0,255),(255,0,255),(255,0,128)]

# create new image filei
iteration =0
image = Image.new("RGB", (imagesize,imagesize))
draw = ImageDraw.Draw(image)
# iterate over all the points in the image
for x in xCoord:
    for y in yCoord:
	iteration =0
	z0 = complex((float(x)-imagesize/2-offsetx)/imagesize*zoom,(float(y)-imagesize/2-offsety)/imagesize*zoom)
	z = complex(0,0)	#z=0+0*j
	#apply equation
	while (iteration < maxiteration and  abs(z*z.conjugate()) < 2**2):
	    z = z**2 + z0
	    iteration = iteration + 1
	#asign color to current point
	if iteration == (maxiteration):
	    asignedcolor = GREEN[0]
	else:
	    asignedcolor = GREEN[iteration%12+1]
	draw.point((x,y),fill=asignedcolor)

# save picture
image.save("Mandelbrot","PNG")

# show picture
image.show()
