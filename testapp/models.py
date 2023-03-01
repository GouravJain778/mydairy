
from django.db import models

# Create your models here.
class mydiary(models.Model):
    id=models.IntegerField(primary_key=True,null=False)
    subject=models.CharField(max_length=20)
    discription=models.CharField(max_length=5000)



