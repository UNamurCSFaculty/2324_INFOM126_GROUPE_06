"""Module for testing views."""
from django.test import TestCase, Client
from django.urls import reverse
from .models import Message
from .forms import MessageForm

"""Class for testing views."""
class MessageListViewTest(TestCase):
    """Function for setting up the test case."""
    def setUp(self):
        self.client = Client()
        self.url = reverse('message-list')

    """Function for testing the GET method of the MessageListView."""
    def test_get_context_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], MessageForm)

    """Function for testing the POST method of the MessageListView."""
    def test_post_valid_form(self):
        data = {
            'text': 'Hello, world!',
            'creator_name': 'John Doe'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('message-list'))

    """Function for testing invalid forms."""
    def test_post_invalid_form(self):
        data = {
            'text': '   Hello, world!   ',
            'creator_name': '123John Doe'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], MessageForm)
        self.assertContains(response, 'Text must start with a letter')

    """Function for testing the invalid forms with leading/trailing whitespaces."""
    def test_post_invalid_form_strip_whitespace(self):
        data = {
            'text': '   Hello, world!   ',
            'creator_name': 'John Doe'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('message-list'))
        self.assertEqual(Message.objects.last().text, 'Hello, world!')
        self.assertEqual(Message.objects.last().creator_name, 'John Doe')