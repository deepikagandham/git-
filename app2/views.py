from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h1>virat is best batsman in the world</h1>')

def deepu(request):
    return HttpResponse('<h2> deepu is a good girl</h2>')
def sample(request):
    return HttpResponse('<h2> hello</h2>')