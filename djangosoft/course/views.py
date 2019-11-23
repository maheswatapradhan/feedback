from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    x="<h1> welcome to Django soft</h1>"
    return HttpResponse(x)
