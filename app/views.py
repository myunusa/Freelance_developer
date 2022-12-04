from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def Index(request):

    return render(request, 'index.html')

def About(request):

    return render(request, 'about.html')

def Members(request):

    return render(request, 'members.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def feed_back(request):
    form=Feedback()
    if request.method =="POST":
        form=Feedback(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    context={
        'form':form
    }
    return render(request, 'feedback.html')