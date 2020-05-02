from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'first_project/index.html')

def home(request):
    return render(request,'first_project/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect('first_project:home')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'first_project/signup.html', context)
