from django.test import TestCase, Client
from django.urls import reverse
from .models import Message
from .forms import MessageForm

class MessageListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('message-list')

    def test_get_context_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], MessageForm)

    def test_post_valid_form(self):
        data = {
            'text': 'Hello, world!',
            'creator_name': 'John Doe'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('message-list'))

    def test_post_invalid_form(self):
        data = {
            'text': '   Hello, world!   ',
            'creator_name': '123John Doe'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], MessageForm)
        self.assertContains(response, 'Text must start with a letter')

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