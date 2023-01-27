from django.db import models

class Item(models.Model):
    url = models.URLField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    is_paid = models.BooleanField(default=False)