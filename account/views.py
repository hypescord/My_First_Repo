from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return HttpResponse('<p> Sign-up page </p>')
def login(request):
    return HttpResponse('<p> Login here </p>')
def password(request):
    return HttpResponse('<p> Forgot Password? </p>')