from django.shortcuts import render, redirect
from item.models import Item, Category
from .forms import SignUpForm, LoginForm

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')

#sign up 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form':form})

# login 
def login(request):
    form = LoginForm()

    return render(request, 'core/login.html', {'form': form})