"""Module for testing forms."""
from django.test import TestCase
from .forms import MessageForm
from .models import Message

"""Module for testing forms."""
class MessageFormTest(TestCase):
    def test_form_fields(self):
        """Check if the form has the correct fields."""
        form = MessageForm()
        self.assertEqual(form.Meta.model, Message)
        self.assertEqual(form.Meta.fields, ['creator_name', 'text'])

    def test_form_valid_data(self):
        """Create valid form data."""
        form_data = {
            'creator_name': 'John Doe',
            'text': 'Hello, world!'
        }

        # Create the form with the valid data
        form = MessageForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        """Create invalid form data."""
        form_data = {
            'creator_name': '123John Doe',
            'text': 'Hello, world!'
        }

        # Create the form with the invalid data
        form = MessageForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())