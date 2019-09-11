from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Card
import logging as logger
# Create your views here.

def index(request):
    template = loader.get_template('inventory/index.html')
    objects = Card.objects.all()
    
    header = [card.__dict__ for card in objects]
    header = [i for i in header[0]][1:]
    
    logger.warning(header)
    return render(request, 'inventory/index.html', {'header':header, 'rows':objects})