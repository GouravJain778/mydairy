
from django.shortcuts import render,HttpResponse,redirect
from .models import mydiary
from django.contrib import messages
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
       return render(request,"testapp/index.html")

def singup(request):
        if request.method=="POST":
                username=request.POST["username"]
                fname=request.POST["fname"]
                lname=request.POST["lname"]
                email=request.POST["email"]
                password=request.POST["password"]
                password=request.POST["password2"]
                myuser=User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
                myuser.save()
                messages.success(request,"your account is created")
                return redirect(singin)
        else:
              return render(request,"testapp/singup.html")
        
def singin(request):
        if request.method=="POST":
                username=request.POST["username"]
                print(username)
                password=request.POST["password"]
                print(password)
                user=authenticate(request,username=username,password=password)
                    
                print(user)
                if user is not None:
                    login(request,user)
                    return redirect(Mydiary)
                else:
                    messages.success(request,"enter valid credential")
                    return redirect(home)
                
                # else:
                #        messages.success(request,"enter valid credential")
                #        return redirect(home)
        
        return render(request,'testapp/singin.html')
               
def singout(request):
       logout(request)
       messages.success(request,"you are logout suusesful")
       return redirect(home)

@login_required(login_url='singin')
def Mydiary(request):
    if request.method=='GET':
        return render(request,'testapp/mydiary.html')
    
    sub=request.POST['subject']
    dis=request.POST['discription']
    obj=mydiary.objects.create(subject=sub,discription=dis)
    obj.save()
    return render(request,'testapp/mydiary.html')
    
def getmydiary(request):
    obj=mydiary.objects.all()
    return render(request,'testapp/acces.html',{'obj':obj})

def updatediary(request,id):
            if request.method=="GET":
                    obj=mydiary.objects.get(id=id)
                    return render(request,'testapp/update.html',{"obj":obj})
            else:
                obj=mydiary.objects.get(id=id)
                sub=request.POST["subject"]
                dis=request.POST["discription"]
                obj.subject=sub
                obj.discription=dis
                obj.save()
                return redirect(getmydiary) 
          
"""delete element in database"""

def delete(request,id):
        obj=mydiary.objects.get(id=id)
        print(obj,"-------------------")
        if request.method=="GET":
            obj.delete()
            return redirect(getmydiary)


                                                                                                                                                                                                                                                                              
