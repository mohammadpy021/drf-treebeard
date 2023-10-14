from django.db import models
from django.contrib.admin.models import LogEntry

# class FootPrint(models.Model):
#     ...

class ActionHistory(LogEntry):
    class Meta:
        proxy = True