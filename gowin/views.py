from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

# Create your views here.
def index(request):
	template = loader.get_template('gowin/index.html')
	return render(request, 'gowin/index.html')