from django.urls import path 
from django.contrib.auth import views as auth_view
from .views import index, contact, signup
from .forms import LoginForm

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm), name='login' ),
    #path('logout/', auth_view.LogoutView.as_view( http_method_names = ['get', 'post', 'options'], template_name='core/logout.html'),name='logout'),
   # path('logout/', logout_view, name='logout')
   path('logout/', auth_view.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
]
