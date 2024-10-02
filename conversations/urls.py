from django.urls import path 

from .views import new_conversation, inbox, detail

urlpatterns = [
    path('', inbox, name='inbox'),
    path('<int:pk>/', detail, name='detail'),
    path('new/<int:item_pk>/', new_conversation, name='new-message'),
]
