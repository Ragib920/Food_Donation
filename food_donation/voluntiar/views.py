from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import VolentiarRegistration,loginForm
from django.contrib import messages
from .models import volentiar
from food_doner.models import Doner_Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = VolentiarRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('user_name')
            messages.success(request,f'You Account has been created! Your are now able to login!!')
            return redirect('Login_Voluntiar')
    else:
        form = VolentiarRegistration()
    return render(request,'voluntiar/reg.html',{'form': form});
def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)

        email = request.POST.get('email')
        passw = request.POST.get('password1')
        ss = volentiar.objects.filter(email=email, password1 = passw)
        if len(ss) == 1:
            return redirect ('volentiar_home')
        else:
            return redirect ('Login_Voluntiar')
    else:
        form = loginForm()
    return render(request, 'voluntiar/login.html', {'form': form});

class PostListView (ListView):
    model = Doner_Post
    template_name = "voluntiar/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostView (DetailView):
    model = Doner_Post
    template_name = "voluntiar/post_view.html"
    #

def change_data(request,pk):
    #pk1=request.GET["pk"];
    obj = Doner_Post.objects.get(pk=pk)
    obj.status = 2
    obj.save()
    return redirect ('volentiar_home')
def change_data1(request,pk):
    #pk1=request.GET["pk"];
    obj = Doner_Post.objects.get(pk=pk)
    obj.status = 1
    obj.save()
    return redirect ('volentiar_home' )
def change_data2(request,pk):
    #pk1=request.GET["pk"];
    obj = Doner_Post.objects.get(pk=pk)
    obj.status = 3
    obj.save()
    return redirect ('volentiar_home')
