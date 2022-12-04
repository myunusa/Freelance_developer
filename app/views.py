from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def Index(request):

    return render(request, 'index.html')

def About(request):

    return render(request, 'about.html')

def Members(request):

    return render(request, 'members.html')

def feed_back(request):
    if request.method =="POST":
        form=Feedback(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    return render(request, 'feedback.html')

def book_project(request):
    if request.method =="POST":
        form=Bookform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    return render(request, 'bookproject.html')