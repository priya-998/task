from django.shortcuts import render
from django. http import HttpResponse
from .forms import registrationforms


from .models import registration,products

# Create your views here.
def index(request):
    return render(request, 'index.html')
def gallery(request):
    dict_pro = {
        'gallery': products.objects.all() 
    }

    
    return render(request, 'gallery.html',dict_pro)
def home(request):
    return render(request, 'home.html')
def details(request):
    return render(request, 'details.html')
    
def registration(request):
    if request.method =="POST":
        forms=registrationforms(request.POST)
        if forms.is_valid():
            forms.save()
            return render(request,'success.html')

    forms = registrationforms()
    dict_forms = {
        'form': forms
    }
    return render(request, 'registration.html',dict_forms)
def update(request):
    return render(request, 'update.html')
def login(request):
     return render(request, 'login.html')    
def changepassword(request):
    return render(request, 'changepassword.html')       