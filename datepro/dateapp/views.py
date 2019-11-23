from django.shortcuts import render
from django.http.response import HttpResponse
import datetime as dt
date=dt.datetime.now()
def dateview(request):
    re="The current date And time is {}".format(date)
    return HttpResponse(re)


