from django.shortcuts import render
from .models import Emp
from .forms import Empform
from django.http.response import HttpResponse

def empview(request):
    if request.method=="POST":
        eform=Empform(request.POST)
        if eform.is_valid():
            name1=request.POST.get('name')
            location1=request.POST.get('location')
            salary1=request.POST.get('salary')
            email1=request.POST.get('email')
            data=Emp(
                name=name1,
                location=location1,
                salary=salary1,
                email=email1
            )
            data.save()
            eform=Empform()
            return render(request,'empform.html',{'eform':eform})
        else:
            return HttpResponse("user invaild data")
    else:
        eform=Empform()
    return render(request,'empform.html',{'eform':eform})