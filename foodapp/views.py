from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def menus(request):
    return render(request,'menus.html')
def plans(request):
    return render(request,'plans.html')
def login(request):
    return render(request,'login.html')
def undercooking(request):
    return render(request,'undercooking.html')