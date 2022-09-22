from django.shortcuts import render

from homeapp.forms import BookingForm
from homeapp.models import Departments, Doctors


def index(request):
    return render(request,'indexpage.html')

def about(request):
    return render(request,'aboutpage.html')

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')

    form=BookingForm()
    dict_form={
     'form':form
    }
    return render(request,'bookingpage.html',dict_form)

def doctor(request):
    dict_doct = {
        'doctors': Doctors.objects.all
    }
    return render(request,'doctorpage.html',dict_doct)

def department(request):
    dict_dept={
        'dept':Departments.objects.all
    }
    return render(request,'departmentpage.html',dict_dept)

def contact(request):
    return render(request,'contactpage.html')



