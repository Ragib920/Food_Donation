from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView,PostView


urlpatterns = [
    path('reg/',views.home,name = "reg"),
    path('login1/', views.login, name='Login_Voluntiar'),
    path('login1/', views.login, name='Login_Voluntiar'),
    path('home/', PostListView.as_view(), name='volentiar_home'),
    path('see_post/<int:pk>/', PostView.as_view(), name='show_post'),
    path('update_status/<int:pk>',views.change_data,name = 'update_status'),
    path('update_status1/<int:pk>', views.change_data1, name='update_status1'),
    path('update_status2/<int:pk>', views.change_data2, name='update_status2'),


]