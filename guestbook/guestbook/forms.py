"""Form Class for the Guestbook App."""
from django import forms
from .models import Message

"""A form for creating a new message in the guestbook."""
class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['creator_name', 'text']
