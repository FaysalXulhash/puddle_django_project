from django import forms
from .models import Item

inp = 'w-full py-4 px-6 rounded-xl border'
class ItemForm(forms.ModelForm):   
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category' : forms.Select(attrs = {
                'class': inp
            }),

            'name' : forms.TextInput(attrs = {
                'class': inp
            }),

            'description' : forms.Textarea(attrs = {
                'class': inp
            }),

            'price' : forms.TextInput(attrs = {
                'class': inp
            }),

            'image' : forms.FileInput(attrs = {
                'class': inp
            }),
        }


#edit from 
class ItemEditForm(forms.ModelForm):   
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category' : forms.Select(attrs = {
                'class': inp
            }),

            'name' : forms.TextInput(attrs = {
                'class': inp
            }),

            'description' : forms.Textarea(attrs = {
                'class': inp
            }),

            'price' : forms.TextInput(attrs = {
                'class': inp
            }),

            'image' : forms.FileInput(attrs = {
                'class': inp
            }),
        }
