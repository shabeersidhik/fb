from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fn_login(request):
    return render(request,'facebookHomePage.html')
def fn_register(req):
    fname=req.POST['firstname']
    lname=req.POST['lastname']
    mobile=req.POST['mobile']
    passw=req.POST['password']
    dob=req.POST['dob']
    gender=req.POST['gender']
    Check_exist=Login.objects.filter(email=mobile).exists()
    if not Check_exist:
        login_obj=Login(email=mobile,password=passw)
        login_obj.save()
        if login_obj.id>0:
            register_obj=Register(firstname=fname,surname=lname,birthday=dob,gender=gender,fk_login=login_obj)
            register_obj.save()
            if register_obj.id>0:
                return HttpResponse('success')
        return HttpResponse('success')
    return HttpResponse('alreadytaken...')