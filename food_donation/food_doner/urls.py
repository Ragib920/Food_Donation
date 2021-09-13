from django.urls import path
from . import views
from .views import PostListView,PostView,PostCreateView, PostUpdateView,PostDelView,UserPostList,PostListView1,PostListView2
urlpatterns = [
    path('', PostListView.as_view(),name = 'food_donation'),
    path('register', views.register, name='registration'),
    path('profile', views.profile, name='profile'),
    path('post/<int:pk>/', PostView.as_view(), name='details'),
    path('post/new/', PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete', PostDelView.as_view(), name='delete'),
    path('mypost', UserPostList.as_view(), name='mypost'),
    path('showallDonor', PostListView1.as_view(),name = 'showall'),
    path('showall', PostListView2.as_view(), name='showall2'),

]
