from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, InventoryLog


from .serializers import ProductSerializer, InventoryLogSerializer
from .service import update_stock


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InventoryLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InventoryLog.objects.all()
    serializer_class = InventoryLogSerializer


@api_view(['GET'])
def update_inventory(request):
    try:
        product_id  = request.data.get('product_id')
        change = int(request.data.get('action'))
        action = request.data.get('action')

        inventory = update_stock(product_id, change, action)

        return Response({
            'message':'Stock is updated',
            'quantity' : inventory.quantity
        })
    
    except Exception as e :
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_stock(request):
    try:
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity'))
        
        inventory = update_stock(product_id, quantity, 'ADD')
        
        return Response({
            'message': 'Stock added successfully',
            'quantity': inventory.quantity
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def remove_stock(request):
    try:
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity'))
        
        inventory = update_stock(product_id, -quantity, 'REMOVE')
        
        return Response({
            'message': 'Stock removed successfully',
            'quantity': inventory.quantity
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


