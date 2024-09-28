from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from .forms import ItemForm

def detail(request, pk):
    items = get_object_or_404(Item, pk=pk)
    rel_item = Item.objects.filter(category=items.category, is_sold=False).exclude(pk=pk)[:3]
    context ={
        'items': items,
        'rel_item': rel_item
    }
    return render(request, 'item/detail.html', context)

@login_required
def newItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item-detail', pk=item.id)
    else:
        form = ItemForm()
    
    return render(request, 'item/item_form.html', {'form': form})