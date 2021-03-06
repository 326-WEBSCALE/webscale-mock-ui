from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User

# Create your models here.
class ApplicationTable(models.Model):
    """
    Model of a table for applications
    """

    api_key = models.CharField('API key', max_length=200, null=True)
    client_id = models.CharField('Client ID', max_length=200, null=True)
    client_secret = models.CharField('Client Secret', max_length=200, null=True)
    contact_email = models.EmailField('Contact Email', max_length=200, help_text="Enter your email")
    copyright_date = models.CharField('Copyright Date', max_length=200, help_text="Enter copyright date")

class Snippit(models.Model):
    """
    Model for representing a Snippit
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Snippit")
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField('Name', max_length=200, help_text="Enter name")
    description = models.TextField(max_length=1000, help_text="Enter the snippit description")
    program_text = models.TextField(max_length=99999, help_text="Enter the program holes")
    program_spec = models.TextField(max_length=99999, help_text="Enter the program spec")

    """
    The synthesizer result needs to be a different kind of model field that will be generated, not entered
    """
    synthesizer_result = models.TextField(max_length=99999, help_text="Enter the synthesizer result")
    is_public = models.BooleanField(default=True, help_text="Toggle for user's public visibility")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

class SnippitData(models.Model):
    """
    Model for Snippit Data
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Snippit Data")
    snippit_id = models.ForeignKey('Snippit', on_delete=models.SET_NULL, null=True)
    synthesizer_time = models.CharField(max_length=200, help_text="Enter time")
    holes_count = models.CharField(max_length=200, help_text="Enter number of holes")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.id)

class HolesTable(models.Model):
    """
    Model for HolesTable
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Holes Table")
    snippit_id = models.ForeignKey('Snippit', on_delete=models.SET_NULL, null=True)
    hole = models.CharField(max_length=200, help_text="Enter hole")
    constant = models.CharField(max_length=200, help_text="Enter constant")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.id)

class GoogleAuth(models.Model):
    """
    Model for Google Authentication
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Google Authentication")
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_authenticated = models.BooleanField(default=True, help_text="Boolean for if user has authorized access to Drive.")
    access_token = models.CharField(max_length=200, help_text="Enter access_token")
    refresh_token = models.CharField(max_length=200, help_text="Enter refresh_token")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.id)

class Comment(models.Model):
    """
    Model for comments
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this comment")
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    snippit_id = models.ForeignKey('Snippit', on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=99999, help_text="Enter the comment text")
    date_posted = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.id)
