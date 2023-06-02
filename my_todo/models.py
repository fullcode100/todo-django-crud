from django.db import models
from datetime import datetime


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=False)
    created_date = models.DateField(default=datetime.now, blank=True)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.title
