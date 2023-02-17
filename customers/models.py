from django.db import models
from accounts.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
