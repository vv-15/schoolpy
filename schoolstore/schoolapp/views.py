from tkinter import Place

from django.shortcuts import render, redirect

#from schoolapp.models import Department


# Create your views here.

# Define your department-Wikipedia mapping here


def home(request):
    return render(request,"index.html")

def computer_science_view(request):
    return render(request, 'computer_science.html')

def commerce_view(request):
    return render(request, 'commerce.html')

def humanities_view(request):
    return render(request, 'humanities.html')

def art_literature_view(request):
    return render(request, 'art_lit.html')

def economics_view(request):
    return render(request, 'economics.html')

def new_page(request):
    return render(request,"new_page.html")