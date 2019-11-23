from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
def home(request):
     x= "<h1> welcome to Django soft</h1>"
     return HttpResponse(x)

