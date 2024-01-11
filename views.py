from django.shortcuts import render,redirect
from .forms import DataForm,EmpForm,EmpModelForm,RegisterUser
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from dbapp.models import Employee,Departmento
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Create your views here.

@login_required(login_url='loginurl')
def firstform(request):
    print(request.x)
    emptyForm=DataForm()
   
    
    if request.method == 'POST':
       # n1=request.POST['t1']
       # n2=request.POST['t2']
        dataform= DataForm(request.POST)
        print(dataform)
        if dataform.is_valid() == True:
            n1=dataform.cleaned_data['name1']
            n2=dataform.cleaned_data['name2']
            
    
            msg='we have recieved data like'+''+n1+''+n2
            return render(request,'formapp/first.html',{'data':msg,'form':emptyForm})
        else:
            #return HttpResponse('data is not valid')
            #print(dataform.errors)
            return render(request,'formapp/first.html',{'form':dataform,'errors':dataform.errors})

    return render(request,'formapp/first.html',{'form':emptyForm})


@login_required(login_url='loginurl')
def employeeform(request):
    emptyForm = EmpForm()
    if request.method == 'POST':
        dataform=EmpForm(request.POST)
        if dataform.is_valid() == True:
            eno=dataform.cleaned_data['empno']
            ename=dataform.cleaned_data['empname']
            esal=dataform.cleaned_data['salary']
            edno=dataform.cleaned_data['department']
            dept=Departmento.objects.filter(deptno=edno)
            if len(dept) > 0:
                 # Employee.objects.create(empno=eno,empname=ename,salary=esal,departmento=dept[0])
                return render(request,'formapp/employee.html',{'form':emptyForm})

            else:
                 return render(request,'formapp/employee.html',{'form':dataform})

            



    return render(request,'formapp/employee.html',{'form':emptyForm})



@login_required(login_url='loginurl')
def employeemodelform(request):
    emptyForm=EmpModelForm()
    if request.method == 'POST':
        dataform=EmpModelForm(request.POST,request.FILES)
        if dataform.is_valid() == True:
            dataform.save()
            return render(request,'formapp/empmodelform.html',{'form':emptyForm})
        else:
             return render(request,'formapp/empmodelform.html',{'form':dataform})

    return render(request,'formapp/empmodelform.html',{'form':emptyForm})

@login_required(login_url='loginurl')
def selectemployee(request):
    #data=Employee.objects.all()
    #return render(request,'formapp/selectemp.html',{'data':data})
   data = Employee.objects.all()
   return render(request,'formapp/selectemp.html',{'data':data})





@login_required(login_url='loginurl')
def detailedinfo(request,eno):
    emp=Employee.objects.get(empno=eno)
    if 'prev_emp' in request.session:
        request.session.modified = True

        request.session['prev_emp'].append(eno)
    else:
        request.session['prev_emp']=[eno]

    print(request.session['prev_emp'])
    prev_emp=Employee.objects.filter(empno__in=request.session['prev_emp'])


    return render(request,'formapp/detail.html',{'employee':emp,'prev_emp':prev_emp})



def homepage(request):
    return render(request,'formapp/home.html')

def loginpage(request):
    if request.method == 'POST':
        uname=request.POST['t1']
        pwd=request.POST['t2']
        validuser=authenticate(request,username=uname,password=pwd)
        if validuser != None:
            login(request,validuser)
            return redirect('homeurl')
        else:
            return redirect('loginurl')

        

    return render(request,'formapp/login.html')


def logoutpage(request):
    logout(request)
    return redirect('loginurl')




def signup(request):
     emptyForm=RegisterUser()
     if request.method == 'POST':
         dataform=RegisterUser(request.POST)
         if dataform.is_valid() == True:
            dataform.save()
            messages.success(request,'user ceated in user table')

            return redirect('loginurl')
         else:
            messages.errors(request,'user creation failed')
            return redirect('signupurl')
     return render(request,'formapp/signup.html',{'form':emptyForm})



