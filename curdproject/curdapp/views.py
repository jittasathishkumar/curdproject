from django.shortcuts import render,redirect
from .models import students

# Create your views here.
def Indexpage(request):
    data=students.objects.all()
    return render(request,'index.html',{'data':data})
    
def add_student(request):
    if request.method=='GET':
        return render(request,'add_student.html')
    else:
        students(
        first_name=request.POST.get('fname'),
        last_name=request.POST.get('lname'),
        mobile_no=request.POST.get('mobile_no'),
        Email=request.POST.get('email'),
        location=request.POST.get('Location'),
        Cgpa=request.POST.get('CGPA'),
        college=request.POST.get('College'),
        ).save()
        return redirect('Indexpage')   

def Update_students(request,id):
    row=students.objects.get(id=id)
    return render(request,'upd.html',{'rows':row})

def upd_data(request,id):
    Data=students.objects.get(id=id)
    Data.first_name=request.POST.get('fname')
    Data.last_name=request.POST.get('lname')
    Data.mobile_no=request.POST.get('mobile_no')
    Data.Email=request.POST.get('email')
    Data.location=request.POST.get('Location')
    Data.Cgpa=request.POST.get('CGPA')
    Data.college=request.POST.get('College')
    Data.save()
    return redirect('Indexpage') 
  
def delete_student(request,id):
    data=students.objects.get(id=id)
    data.delete()
    return redirect('Indexpage')

        
