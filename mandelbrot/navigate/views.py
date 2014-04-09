from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader 

import imageAdministrator

def generatePage(request):
    """Generic template code"""

# Create your views here.
def index(request):
    return HttpResponse("Something")

def home(request):
    """Shows the default image as starting point"""

    currImage = imageAdministrator.ImageAdministrator()
    currImage.calculate_mandelbrot('/Users/andreakramm/Pythonprojects/Mandelbrot/mandelbrot/navigate/static/navigate/images/Mandelbrot.png')

    # a_list = Article.objects.filter(pub_date__year=year) 
    # context = {'year': year, 'article_list': a_list}
    template = loader.get_template('navigate/home.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
    # return render(request, 'navigate/mandelbrotTemplate.html', context)

def generateImageAt(request):
    """For a given URL parse and validity check parameters and 
        generate the appropriate image. Send to home if invalid params."""

def navigateTo(request, **imageParams):
    """Parse the starting point parameters from the url, change them
        depending on the data from the post request"""
    currImage = imageAdministrator.ImageAdministrator(imageParams['xCoord'], imageParams['yCoord'], imageParams['zoom'])
    if request.method == "POST":
        # TODO for each type of post
        currImage.change_offset_and_zoom(int(request.POST['zoom_offset.x']), int(request.POST['zoom_offset.y']))

    currImage.calculate_mandelbrot('/Users/andreakramm/Pythonprojects/Mandelbrot/mandelbrot/navigate/static/navigate/images/Mandelbrot.png')
    return home(request)


    #TODO redirect to new params
