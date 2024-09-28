from django.urls import path 
from django.contrib.auth import views as auth_view
from .views import index, contact, signup, login

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    #path('login/', login, name='login'),
    path('login/', auth_view.LoginView.as_view(template_name = 'core/login.html'), name='login' ),
]
