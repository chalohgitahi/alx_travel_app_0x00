from django.db import models
import uuid


class User(models.Model):
    user_id = models.UUIDField(primary_key = True, default = uuid.uuid4, db_index=True)
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    email = models.CharField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=36)
    role = models.TextChoices('role', 'guest host admin')
    created_at = models.DateField()
    

class Message(models.Model):
    message_id = models.UUIDField(primary_key = True, default = uuid.uuid4, db_index=True)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message_body = models.TextField()
    sent_at = models.DateField()


class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key = True, default = uuid.uuid4, db_index=True)
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()


