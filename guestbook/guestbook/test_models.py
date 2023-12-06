from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Message

class MessageModelTest(TestCase):
    def test_message_creation(self):
        # Create a message
        message = Message.objects.create(
            text="Hello, world!",
            creator_name="John Doe"
        )

        # Check if the message is created successfully
        self.assertEqual(message.text, "Hello, world!")
        self.assertEqual(message.creator_name, "John Doe")
        self.assertIsNotNone(message.created_at)

    def test_message_clean_method(self):
        # Create a message with leading/trailing whitespaces and an invalid creator name
        message = Message(
            text="   Hello, world!   ",
            creator_name="John Doe"
        )

        # Clean the message
        message.clean()

        # Check if the leading/trailing whitespaces are stripped
        self.assertEqual(message.text, "Hello, world!")
        self.assertEqual(message.creator_name, "John Doe")

        # Check if the validation error is raised for an invalid creator name
        with self.assertRaises(ValidationError):
            message.creator_name = "123John Doe"
            message.clean()

    def test_message_save_method(self):
        # Create a message
        message = Message(
            text="Hello, world!",
            creator_name="John Doe"
        )

        # Save the message
        message.save()

        # Check if the message is saved successfully
        saved_message = Message.objects.get(pk=message.pk)
        self.assertEqual(saved_message.text, "Hello, world!")
        self.assertEqual(saved_message.creator_name, "John Doe")
        self.assertIsNotNone(saved_message.created_at)