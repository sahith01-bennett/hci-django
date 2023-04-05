from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from events.models import EventCategory, Event, UserSystem
from .forms import LoginForm

@login_required(login_url='login')
def dashboard(request):
    user = User.objects.count()
    event_ctg = EventCategory.objects.count()
    event = Event.objects.count()
    complete_event = Event.objects.filter(status='completed').count()
    events = Event.objects.all()
    context = {
        'user': user,
        'event_ctg': event_ctg,
        'event': event,
        'complete_event': complete_event,
        'events': events
    }
    return render(request, 'dashboard.html', context)

def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            print("hello")
            print(username)
            # try:
            #     response = UserSystem.objects.get(username=username)
            #     print(response)
            #     if response:
            #         print("Here")
            #         return redirect('dashboard')
            #         # login(request, username)
                    
            # except:
            #     print("Not a user")

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {
        'form': forms
    }
    return render(request, 'login.html', context)

def logut_page(request):
    logout(request)
    return redirect('login')

def register_user(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            print("Trying to store")
            print(username)
            print(password)
            obj = User.objects.create_user(username=username, password=password)
            obj.save()
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')

            # obj = UserSystem(username=username, password=password)
            # obj.save()
            # reg = forms.save()
            # print(forms.cleaned_data)
            # Users.objects.create(**forms.cleaned_data)
            # response = User.objects.get(username=username)
            # print(response)
            # if response:
            #     # login(request, username)
            #     return redirect('dashboard')
            # else:
            #     user = authenticate(username=username, password=password)
            #     if user:
            #         login(request, user)
            #         return redirect('dashboard')
    context = {
        'form': forms
    }
    return render(request, 'register.html', context)