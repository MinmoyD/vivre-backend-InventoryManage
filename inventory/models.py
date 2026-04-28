from django.db import models

class Product(models.Model):
    name =  models.CharField(max_length=100)
    sku = models.CharField(max_length=255 , unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class InventoryLog(models.Model):
    TYPE_CHOICE = (
        ('ADD', 'Add'),
        ('REMOVE', 'Remove'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

