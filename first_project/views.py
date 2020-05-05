from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import User
from django.views.generic import DetailView,UpdateView
from .forms import UserForm
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
            return redirect('first_project:list')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'first_project/signup.html', context)

def list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'first_project/list.html',context)

def listdetail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post}
    return render(request,'first_project/listdetail.html',context)


def listcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('first_project:list')
    else:
        form = PostForm()
    return render(request,'first_project/listcreate.html',{'form':form})

@require_POST
def listdelete(request,pk):
    memo = get_object_or_404(Post,pk=pk)
    memo.delete()
    return redirect('first_project:list')

def listupdate(request,pk):
    memo = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=memo)
        if form.is_valid():
            form.save()
            return redirect('first_project:list')
    else:
        form = PostForm(instance=memo)
    return render(request,'first_project/listupdate.html',{'form':form,'memo':memo})

class UserDetailView(DetailView):
    model = User
    template_name = 'first_project/userdetail.html'

class UserUpdateView(UpdateView):
    model = User
    template_name = 'first_project/userupdate.html'
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('first_project:userdetail',pk=self.kwargs['pk'])
