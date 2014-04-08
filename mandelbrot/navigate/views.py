from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader 

def generatePage(request):
    """Generic template code"""

# Create your views here.
def index(request):
    return HttpResponse("Something")

def home(request):
    """Shows the default image as starting point"""
    if request.method == "POST":
        print request.POST


    #TODO get previous url and the parameters therein, and init imageAdmin 

    #TODO generate image


    # a_list = Article.objects.filter(pub_date__year=year) 
    # context = {'year': year, 'article_list': a_list}
    template = loader.get_template('navigate/home.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
    # return render(request, 'navigate/mandelbrotTemplate.html', context)

def generateImageAt(request):
    """For a given URL parse and validity check parameters and 
        generate the appropriate image. Send to home if invalid params."""

def navigateTo(request, coordinates):
    """Parse the starting point parameters from the url, change them
        depending on the data from the post request"""
    print coordinates
    return home(request)
    #TODO get previous url and the parameters therein, and init imageAdmin 

    #TODO depending on the post data call imageAdmin and change params

    #TODO redirect to new params
