from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Doner_Post
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from voluntiar.models import volentiar
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    context = {
        'posts' : Doner_Post.objects.all()
    }
    return render(request,'food_doner/home.html', context);
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'You Account has been created! Your are now able to login!!')
            return redirect('food_donation')
    else:
        form = UserRegisterForm()
    return  render(request,'food_doner/register.html',{'form': form});


class PostListView (ListView):
    model = Doner_Post
    template_name = "food_doner/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
class PostListView1 (ListView):
    model = User
    template_name = "food_doner/showall.html"
    context_object_name = 'posts'

class PostListView2 (ListView):
    model = volentiar
    template_name = "food_doner/showall2.html"
    context_object_name = 'posts'
class PostView (DetailView):
    model = Doner_Post
    template_name = "food_doner/post_view.html"

class PostDelView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Doner_Post
    success_url = '/'
    template_name = "food_doner/post_Delete.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        return False

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Doner_Post
    fields = ['date','title','food_des']
    template_name = 'food_doner/post_form.html'
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Doner_Post
    fields = ['date','title','food_des']
    template_name = 'food_doner/post_form.html'
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        return False


class UserPostList(LoginRequiredMixin, ListView):
    context_object_name = 'posts'
    template_name = 'doner_post_list.html'

    def get_queryset(self):
        return Doner_Post.objects.filter(username=self.request.user)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance= request.user)
        p_form=  ProfileUpdateForm(request.POST,request.FILES,instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You Account has been updated!!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form' : p_form
    }
    return  render(request,'food_doner/profile.html',context);
