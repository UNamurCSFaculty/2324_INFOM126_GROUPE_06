from django.db import models
from django.core.exceptions import ValidationError

class Message(models.Model):
    """
    Represents a message in the guestbook.

    Attributes:
        text (str): The content of the message.
        creator_name (str): The name of the message creator.
        created_at (datetime): The timestamp when the message was created.
    """

    text = models.TextField(blank=False, null=False)
    creator_name = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
    
    def clean(self) -> None:
        """
        Clean method for the Message model.
        It strips leading and trailing whitespaces from the text and 
        creator_name fields.
        It also validates that the creator_name starts with a letter.
        """
        self.text = self.text.strip()
        self.creator_name = self.creator_name.strip()
        if not self.creator_name[0].isalpha():
            raise ValidationError('Text must start with a letter')
        super().clean()

    def save(self, *args, **kwargs) -> None:
        """
        Save the model instance after performing full_clean().

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            None
        """
        self.full_clean()
        super().save(*args, **kwargs)