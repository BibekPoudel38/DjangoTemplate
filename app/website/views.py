from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.


def index(request):
    html_template = loader.get_template('home/index.html')
    context = {
        'page': 'index',
    }
    return HttpResponse(html_template.render(context, request))
