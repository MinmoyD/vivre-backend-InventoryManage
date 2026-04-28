from django.db import transaction
from django.core.exceptions import ValidationError

from .models import Product, InventoryLog


def update_stock(product_id, quantity, action_type):
    with transaction.atomic():
        product = Product.objects.select_for_update().get(pk=product_id)
        new_quantity = product.quantity + quantity

        if new_quantity < 0:
            raise ValidationError("Stock cannot be negative")
        
        product.quantity = new_quantity 
        product.save()
        
        InventoryLog.objects.create(
            product=product,
            type=action_type,
            quantity=quantity
        )

        return product