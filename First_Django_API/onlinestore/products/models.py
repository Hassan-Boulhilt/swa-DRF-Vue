from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    def shipping(self):
        shipping = self.price * 5/100
        return shipping
    def totalcost(self):
        return (self.price+ self.shipping())*self.quantity
        
