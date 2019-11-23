from django.shortcuts import render
from .models import EnquaryData
from .forms import EnquryForm
from django.http.response import HttpResponse
def EnquryView(request):
    if request.method=="POST":
        eform=EnquryForm(request.POST)
        if eform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            course=eform.cleaned_data.get('course')
            location=eform.cleaned_data.get('location')
            gender=eform.cleaned_data.get('gender')
            start_date=eform.cleaned_data.get('start_date')
            data=EnquaryData(
                name=name,
                email=email,
                mobile=mobile,
                course=course,
                location=location,
                gender=gender,
                start_date=start_date
            )
            data.save()
            eform=EnquryForm()
            return render(request,'enqury.html',{'eform':eform})
        else:
            return HttpResponse("user Invaild Data")
    else:
        eform=EnquryForm()
        return render(request,'enqury.html',{'eform':eform})


