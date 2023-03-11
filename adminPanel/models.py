from django.db import models

# Create your models here.

class Auth(models.Model):
    id          = models.AutoField(primary_key=True)
    auth_id     = models.CharField(max_length=50, blank=True, null=True)
    blong_to    = models.CharField(max_length=200, blank=True, null=True)
    
