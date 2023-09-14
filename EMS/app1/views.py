from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponseRedirect
from app1.models import *

# ------------user's views----------------
def homepage(req):
    return render(req,'home.html')
def ureges(req):
    return render(req,'ureges.html')
def uinsert(req):
    if req.method=="POST":
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        email=req.POST.get('email')
        cont=req.POST.get('contact')
        passw=req.POST.get('passw')
        cpassw=req.POST.get('cpassw')
        user=UDB.objects.filter(Email=email)
        print(user)
        if user:
            msg="USER ALREADY EXISTS"
            return render(req,"ureges.html",{"msg":msg})
        else:
            if passw==cpassw:
                user1=UDB(Firstname=fname,Lastname=lname,Email=email,
                                                    Contact=cont,Password=passw)
                user1.save()
                msg="User entered successfully"
                return render(req,"home.html",{'msg':msg})
            else:
                msg='Password does not matched'
                return render(req,"ureges.html",{"msg":msg})
    return render(req,"ureges.html")

def uloginp(req):
    return render(req,"userlog.html")

def userlogin(req):
    if req.method=='POST':
        email=req.POST.get('email')
        passw=req.POST.get('passw')
        user=UDB.objects.get(Email=email)
        if user:
            if user.Password==passw:
                user1=UDB(Email=email,Password=passw)
                print(user1)
                return render(req,"userdashb.html")
            else:
               msg="Invalid Email Or Password"
               return render(req,"userlog.html",{"msg":msg}) 
                    
    msg="User Doesn't Exists!"
    return render(req,"ureges.html",{"msg":msg})



# ------------admin's views----------------

def areges(req):
    return render(req,"areges.html")

def ainsert(req):
    if req.method=="POST":
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        cont=req.POST.get('contact')
        email=req.POST.get('email')
        passw=req.POST.get('passw')
        cpassw=req.POST.get('cpassw')
        user=ADB.objects.filter(Email=email)
        if user:
            msg="User Already Exists!"
            return render(req,"areges.html",{"msg":msg})
        else:
            if passw==cpassw:
              user1=ADB(Firstname=fname,Lastname=lname,Email=email,Contact=cont,Password=passw)
              user1.save()
              msg="User Entered Successfully."
              return render(req,"home.html",{"msg":msg})
            else:
                msg="Password Doesnt Match"
                return render(req,"areges.html",{"msg":msg})
    return render(req,"areges.html")

def aloginp(req):
    return render(req,'adminlog.html')

def adminlogin(req):
    if req.method=="POST":
        email=req.POST.get('email')
        passw=req.POST.get('passw')
        user=ADB.objects.get(Email=email)
        if user:
            if user.Password==passw:
                user1=ADB(Email=email,Password=passw)
                print(user1)
                return render(req,"admindashb.html")
            else:
               msg="Password or Email does not match"
               return render(req,"adminlog.html",{"msg":msg})

    msg="User Does Not Exists"
    return render(req,"areges.html",{"msg":msg})

#------------------enquiry---------------------
def enquiry(req):
    return render(req,"enquiry.html")

def einsert(req):
    if req.method=="POST":
        sname=req.POST.get('sname')
        cont=req.POST.get('contact')
        email=req.POST.get('email')
        enquiry=req.POST.get('enquiry')
        user=EDB(Stuname=sname,Email=email,Contact=cont,Enquiry=enquiry)
        user.save()
        msg="Enquiry Successfully"
        return render(req,"home.html",{"msg":msg})
    
#-----------------------crud--------------------

def display(req):
    data=EDB.objects.all()
    return render(req,"display.html",{"data":data})

def EditPage(request,id):
    data=EDB.objects.get(id=id)
    return render(request,'update.html',{'data':data})


def update(req,id):
    user=EDB.objects.get(id=id)
    sname=req.POST.get('sname')
    cont=req.POST.get('contact')
    email=req.POST.get('email')
    enquiry=req.POST.get('enquiry')
    user=EDB(id=id,Stuname=sname,Email=email,Contact=cont,Enquiry=enquiry)
    user.save()
    return HttpResponseRedirect(req,"display.html")

def delete(req,id):
    data=EDB.objects.get(id=id)
    data.delete()
    return redirect(req,"display.html")



