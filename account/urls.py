from django.urls import path
from .views import login, signup, password

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('password/', password)
]