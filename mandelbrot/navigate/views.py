from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader 

import imageAdministrator

def generatePage(request):
    """Generic template code"""
    # a_list = Article.objects.filter(pub_date__year=year) 
    # context = {'year': year, 'article_list': a_list}
    template = loader.get_template('navigate/home.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def redirectUsing(request, currImage):
    """Redirect depending on the parsed post parameters"""
    print request.POST
    # TODO for each type of post
    # offset_and_zoom
    # zoom
    # offset
    # change size
    # change colors
    # change iteration depth
    # TODO do a validity check 
    currImage.change_offset_and_zoom(int(request.POST['zoom_offset.x']), int(request.POST['zoom_offset.y']))
    return HttpResponseRedirect('/navigate/@%s,%s,z%s/%s/%s/i%s/c%s'%currImage.get_center())


# List of views
def index(request):
    return HttpResponse("Something")

def home(request):
    """Shows the default image as starting point"""
    currImage = imageAdministrator.ImageAdministrator()
    # TODO change to generic file path, production? 
    currImage.calculate_mandelbrot('/Users/demo/Desktop/mandelbrot/Mandelbrot/mandelbrot/navigate/static/navigate/images/Mandelbrot.png')
    if request.method == "POST":
        return redirectUsing(request, currImage)
    return generatePage(request)

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
    currImage.calculate_mandelbrot('/Users/demo/Desktop/mandelbrot/Mandelbrot/mandelbrot/navigate/static/navigate/images/Mandelbrot.png')
    return generatePage(request)

