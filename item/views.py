from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from .forms import ItemForm, ItemEditForm

def detail(request, pk):
    items = get_object_or_404(Item, pk=pk)
    rel_item = Item.objects.filter(category=items.category, is_sold=False).exclude(pk=pk)[:3]
    context ={
        'items': items,
        'rel_item': rel_item
    }
    return render(request, 'item/detail.html', context)

# create new item
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

# delete item 
@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk= pk)
    item.delete()
    return redirect('home')

@login_required
def edit_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemEditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item-detail', pk=pk)
    else:
        form = ItemEditForm(instance = item)
    return render(request, 'item/edit_form.html', {'form': form})