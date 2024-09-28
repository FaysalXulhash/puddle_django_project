from django.urls import path 
from .views import detail, newItem


urlpatterns = [
    path('<int:pk>/', detail, name='item-detail'),
    path('new/', newItem, name='new-item'),
    
]
