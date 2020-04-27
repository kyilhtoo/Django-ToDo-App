from django.db import models
from django.urls import reverse


class Tasks(models.Model):
    task_name = models.TextField(max_length=300)
    task_detail = models.TextField()

    def __str__(self):
        return self.task_name
