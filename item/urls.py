from django.urls import path 
from .views import detail, newItem, delete_item, edit_item


urlpatterns = [
    path('<int:pk>/', detail, name='item-detail'),
    path('new/', newItem, name='new-item'),
    path('<int:pk>/delete/', delete_item, name='delete'),
    path('<int:pk>/edit/', edit_item, name='edit'),
    
]
