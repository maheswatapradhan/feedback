from django.shortcuts import render
from django.http.response import  HttpResponse
def home(request):
    x="welcome to Django"
    return HttpResponse(x)
def contact(request):
    x="my contact no is123456"
    return HttpResponse(x)
def services(request):
    x="we provides all services"
    return HttpResponse(x)
def feedback(request):
    x="we have good feedback"
    return HttpResponse(x)

