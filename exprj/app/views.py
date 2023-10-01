from django.shortcuts import redirect, render
from .models import StdForm
from exprj.urls import *

def home(request):
    return render(request, '../templates/index.html')

def createform(request):
    posts = StdForm.objects.all()
    return render(request, '../templates/index.html', {'posts': posts})