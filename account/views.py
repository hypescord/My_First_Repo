from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request, "account/register.html")
def login(request):
    return render(request, "account/login.html")
def password(request):
    return render(request, "account/password.html")