from django.db import models

# Create your models here.

class Bug(models.Model):
    name = models.CharField('bug名称', max_length=100)