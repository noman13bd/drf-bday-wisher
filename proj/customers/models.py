from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    bday = models.DateField()
    notified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
