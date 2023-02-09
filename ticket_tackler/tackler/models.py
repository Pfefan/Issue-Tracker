"""
This module is the database models for a Issue Tracking system.
"""
from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    """
    A class representing a ticket in the ticketing system.
    """
    ticket_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=100)
    relevance = models.CharField(max_length=25)
    status = models.CharField(max_length=50, default='Open')
    is_open = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets')
    assigned_users = models.ManyToManyField(User, related_name='assigned_tickets')

class Ticket_Comments(models.Model):
    """
    A class representing a comment on a ticket in the ticketing system.
    """
    reply_id = models.AutoField(primary_key=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey("Ticket", on_delete=models.CASCADE)
