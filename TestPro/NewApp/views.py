from django.shortcuts import render,redirect
from .models import News
from .forms import RegistrationForm,RegistrationModel
from .models import RegistrationData
from django.contrib import messages
# Create your views here.

def NewsPage(Request):
    obj = News.objects.get(id = 1)
    context = {
        "data": obj
    }
    return render(Request,'news.html',context)

def NewsDate(request,year):
    article_list = News.objects.filter(pub_date__year=year)
    context={
        'year':year,
        'article_list':article_list
    }
    return render(request,'newsdate.html',context)

def Home(request):
    data = {"name":"Suresh",
    "number": 9824785214}
    return render(request,'home.html',data)

def Contact(Request):
    return render(Request,'contact.html')

def SignUp(request):
    context={
        "form":RegistrationForm
    }
    return render(request,'signup.html',context)



def AddUser(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        myregister = RegistrationData(username = form.cleaned_data['username'],
        password = form.cleaned_data['password'],
        email = form.cleaned_data['email'],
        phone = form.cleaned_data['phone'],
        )
        myregister.save()
        messages.add_message(request,messages.SUCCESS,"You have signup Successfully")
    return redirect('register')

def ModelForm(request):
    context={
        "modelform":RegistrationModel
    }
    return render(request,'modelform.html',context)

def addModelForm(request):
    mymodalform = RegistrationModel(request.POST)
    if mymodalform.is_valid():
        mymodalform.save()
    return redirect('modelform')
