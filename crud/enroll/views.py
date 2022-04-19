from django.shortcuts import render,HttpResponseRedirect
from.forms import Student
from .models import User
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=Student(request.POST)
        if fm.is_valid():
           nm= fm.cleaned_data['name']
           em=fm.cleaned_data['email']
           pwd=fm.cleaned_data['password']
           reg=User(name=nm,email=em,password=pwd)
           reg.save()
           fm=Student()
    else:
        fm=Student()
    stud=User.objects.all()
    return render(request,'enroll/add.html',{'form':fm,'stu':stud})

def update(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=Student(request.POST,instance=pi)
        if fm.is_valid():
          fm.save()
        else:
         pi=User.objects.get(pk=id)
        fm=Student(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})

def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
