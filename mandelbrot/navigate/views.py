from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader 


# Create your views here.
def index(request):
    return HttpResponse("Something")

def home(request):
    # a_list = Article.objects.filter(pub_date__year=year) 
    # context = {'year': year, 'article_list': a_list}
    template = loader.get_template('navigate/home.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
    # return render(request, 'navigate/mandelbrotTemplate.html', context)

# def results(request, poll_id):