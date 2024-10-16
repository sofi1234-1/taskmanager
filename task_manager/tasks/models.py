from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

PRIORITY_CHOICES = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
]

STATUS_CHOICES = [
    ('P', 'Pending'),
    ('C', 'Completed'),
]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.title

    def is_due(self):
        return self.due_date < timezone.now()

    def mark_complete(self):
        self.status = 'C'
        self.completed_at = timezone.now()
        self.save()

    def mark_incomplete(self):
        self.status = 'P'
        self.completed_at = None
        self.save()


