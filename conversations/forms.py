from django import forms

from .models import Conversations, ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    
    class Meta:
        model = ConversationMessage
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs = {
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }
        labels = {
            'content': 'Message',
        }
