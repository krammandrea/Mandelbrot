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
    return HttpResponseRedirect('/navigate/@%s,%s,z%s'%currImage.get_center())


# List of views
def index(request):
    return HttpResponse("Something")

def home(request):
    """Shows the default image as starting point"""
    currImage = imageAdministrator.ImageAdministrator()
    currImage.calculate_mandelbrot('/Users/andreakramm/Pythonprojects/Mandelbrot/mandelbrot/navigate/static/navigate/images/Mandelbrot.png')
    if request.method == "POST":
        return redirectUsing(request, currImage)
    return generatePage(request)

def navigateTo(request, **imageParams):
    """Take the starting point parameters from the url, change them
        depending on the data from the post request"""
    currImage = imageAdministrator.ImageAdministrator(imageParams['xCoord'], imageParams['yCoord'], imageParams['zoom'])
    if request.method == "POST":
        return redirectUsing(request, currImage)
    currImage.calculate_mandelbrot('/Users/andreakramm/Pythonprojects/Mandelbrot/mandelbrot/navigate/static/navigate/images/Mandelbrot.png')
    return generatePage(request)

