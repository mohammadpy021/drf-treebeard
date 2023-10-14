from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class AuditableModel(models.Model):
    created_by  = models.ForeignKey(get_user_model(), related_name="created", on_delete=models.SET_NULL, null=True, editable=False) #settings.AUTH_USER_MODEL
    created_at  = models.DateField(auto_now_add= True, editable=False)
    modified_by = models.ForeignKey(get_user_model(), related_name="modified", on_delete=models.SET_NULL, null=True, editable=False)
    modified_at = models.DateField(auto_now=True,   editable=False)
    
    class Meta:
        abstract = True #abstract model