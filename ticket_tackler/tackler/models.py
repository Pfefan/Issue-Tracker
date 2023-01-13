from django.db import models


class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    topic = models.CharField(max_length=100)
    relevance = models.CharField(max_length=100)
    resolved = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

class Ticket_Replies(models.Model):
    reply_id = models.IntegerField(primary_key=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    ticket_id = models.ForeignKey("Ticket", on_delete=models.CASCADE)

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    Admin = models.BooleanField()
