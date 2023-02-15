from django.db import models

class Pizza(models.Model):
    
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Toppings(models.Model):

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Create your models here.
