from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    """
    A form for creating a new message in the guestbook.
    """
    class Meta:
        model = Message
        fields = ['creator_name', 'text']
