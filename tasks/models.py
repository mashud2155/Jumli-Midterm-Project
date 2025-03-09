from django.db import models
from django.utils import timezone
from datetime import datetime, date

class Task(models.Model):
    # define the fields for the task model
    title = models.CharField(max_length=200)  # title of the task
    description = models.TextField()  # description of the task
    due_date = models.DateField(null=True, blank=True)  # due date of the task, can be empty
    status = models.CharField(max_length=20, default='pending')  # status of the task, default is 'pending'

    def __str__(self):
        # return the title of the task when the object is printed
        return self.title

    def save(self, *args, **kwargs):
        # call the save method of the parent class
        super().save(*args, **kwargs)

    def check_and_update_overdue_status(self):
        # check if the task is overdue and update the status
        if self.due_date:
            if isinstance(self.due_date, datetime):
                due_date = self.due_date
            elif isinstance(self.due_date, date):
                # convert date to datetime and make it timezone aware
                due_date = datetime.combine(self.due_date, datetime.min.time())
                due_date = timezone.make_aware(due_date, timezone.get_current_timezone())
            # if the due date is in the past, mark the task as overdue
            if due_date < timezone.now():
                self.status = 'overdue'
                self.save()

from django import forms
from .models import Task