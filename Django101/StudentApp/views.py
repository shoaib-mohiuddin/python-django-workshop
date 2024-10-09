from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def hello1(request):
    return HttpResponse("<h1>Hello, world! This is the first view.</h1>")

def hello2(request):
    template=loader.get_template("welcome.html")
    return HttpResponse(template.render())

def hello3(request):
    template=loader.get_template("home.html")
    context={
        'fname':'Jon',
        'cmp':'Eviden'
    }

    return HttpResponse(template.render(context))

def hello4(request):
    context=[
        {'name':'Jon', 'value':100},
        {'name':'Rob', 'value':200},
        {'name':'Bran', 'value':300}
    ]
    return render(request, 'page.html', {'employees': context})