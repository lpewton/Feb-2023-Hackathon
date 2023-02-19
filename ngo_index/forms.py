from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Message


class MessageForm(forms.ModelForm):
    """
    Form for allowing a user to submit a message
    """
    class Meta:
        model = Message
        fields = ('first_name', 'last_name', 'email_address', 'message')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            'email_address': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your message'
            })
        }
