from django.shortcuts import render
from .models import GroceryItem

def index(request):
    items = GroceryItem.objects.all()
    return render(request, 'grocery/index.html', {'items': items})