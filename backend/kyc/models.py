from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=20)  # merchant / reviewer

class KYCSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(default='draft', max_length=50)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    business_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=50)
    volume = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    submission = models.ForeignKey(KYCSubmission, on_delete=models.CASCADE)
    file = models.FileField(upload_to='docs/')

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)