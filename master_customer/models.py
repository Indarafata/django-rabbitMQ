from django.db import models

from datetime import date

class MasterCustomer(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    created_at = models.DateField(default=date.today)
    
    