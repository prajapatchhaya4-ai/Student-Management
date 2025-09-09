from django.shortcuts import render,redirect
from .forms import Stdform
from .models import Student

# Create your views heref
def add(request):
   stdform=Stdform()
   return render(request,'add.html',{'stdform':stdform})

def insert(request):
   if request.method=="POST":
       stdform=Stdform(request.POST)
       if stdform.is_valid():
         stdform.save()
         return render(request,'signup.html')
       else:
         return render(request,'add.html')
   else:
      return render(request,'add.html')   
   
def show(request):
   students=Student.objects.all()
   return render(request, 'show.html',{'students':students})   

def edit(request,rollnumber):
   std=Student.objects.get(rollnumber=rollnumber)
   return render(request,'edit.html',{'std':std})

def update(request,rollnumber):
   if request.method=='POST':
      std=Student.objects.get(rollnumber=rollnumber)
      form=Stdform(request.POST,instance=std)
      if form.is_valid():
         form.save()
         return redirect ('show')
      else:
         return render(request,'edit.html', {'std':std})
   else:
       return render(request,'edit.html', {'std':std})   
   
def delete(request,rollnumber):
      std=Student.objects.get(rollnumber=rollnumber)
      std.delete()
      return redirect('add')


