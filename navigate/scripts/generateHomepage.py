
from django.template import RequestContext, loader 

template = loader.get_template('navigate/home.html')
context = RequestContext(request, templateParams)
return template.render(context)
