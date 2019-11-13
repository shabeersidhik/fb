from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fn_login(request):
    return render(request,'facebookHomePage.html')
    