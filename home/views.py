from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1> my home page </h1>')
def about(request):
    return HttpResponse('<h1> about us </h1>')
def contact(request):
    return HttpResponse('<h1> contact us </h1>')