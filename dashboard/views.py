from django.shortcuts import render
from item.models import Item 


def home(request):
    items = Item.objects.filter(created_by = request.user)

    return render(request, 'dashboard/home.html', {'items': items})