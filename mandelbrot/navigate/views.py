from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader 

import imageAdministrator

# Helper functions
def generateImageAndPage(request, currImage):
    """Calculate current Mandelbrot image and generate page"""
    imageName = 'Mandelbrot_%s.png' %str(currImage.generate_hashSum()) 
    # TODO change to generic file path, production? 
    currImage.calculate_mandelbrot('/Users/andreakramm/Pythonprojects/Mandelbrot/mandelbrot/navigate/static/navigate/images/%s'%imageName)
    templateParams = {'imageName': imageName}
    return generatePage(request, templateParams)

def generatePage(request, templateParams):
    """Generic template code"""
    template = loader.get_template('navigate/home.html')
    context = RequestContext(request, templateParams)
    return HttpResponse(template.render(context))

def redirectUsing(request, currImage):
    """Redirect depending on the parsed post parameters"""
    if 'zoom_offset.x' in request.POST:
        currImage.change_offset_and_zoom(int(request.POST['zoom_offset.x']), int(request.POST['zoom_offset.y']))
    elif 'offset_right.x' in request.POST:
        currImage.change_offset(1,0)
    elif 'offset_left.x' in request.POST:
        currImage.change_offset(-1,0)
    elif 'offset_up.x' in request.POST:
        currImage.change_offset(0,-1)
    elif 'offset_down.x' in request.POST:
        currImage.change_offset(0,1)
    elif 'z' in request.POST:
        currImage.change_zoom(2**((int(request.POST['z'][0]))-5))
    elif 'zoom_in' in request.POST:
        currImage.change_zoom(2.0)
    # TODO fix maximum zoomout
    elif 'zoom_out' in request.POST:
        currImage.change_zoom(0.5)
    elif 'pxheight' in request.POST:
        currImage.change_imagesize(int(request.POST['pxwidth']), int(request.POST['pxheight']))
    elif 'iter' in request.POST:
        currImage.change_maxiteration(int(request.POST['iter']))
    elif 'col' in request.POST:
        print dir(request.POST)
        currImage.change_colorscheme(request.POST.getlist('col'))

    return HttpResponseRedirect('/navigate/@%s,%s,z%s/%s/%s/i%s/c%s'%currImage.get_center())


# List of views
def index(request):
    return HttpResponse("Something")

def home(request):
    """Shows the default image as starting point"""
    currImage = imageAdministrator.ImageAdministrator()
    if request.method == "POST":
        return redirectUsing(request, currImage)
    return generateImageAndPage(request, currImage)

def navigateTo(request, **imageParams):
    """Take the starting point parameters from the url, validate and parse them, change them
    depending on the data from the post request"""
    valParams = imageAdministrator.ImageAdministrator.validate_and_parse_all_params(imageParams)
    currImage = imageAdministrator.ImageAdministrator(
            xCoord = valParams['xCoord'], 
            yCoord = valParams['yCoord'], 
            zoom = valParams['zoom'], 
            xSize = valParams['xSize'], 
            ySize = valParams['ySize'], 
            iterations = valParams['iterations'],
            colors = valParams['colors'])
    if request.method == "POST":
        return redirectUsing(request, currImage)
    return generateImageAndPage(request, currImage)

