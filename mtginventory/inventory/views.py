from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Card, Player, States, Colour, Expansion
import logging as logger
# Create your views here.

def index(request):
    template = loader.get_template('inventory/index.html')
    objects = Card.objects.all()
    items=list()

    objects = [card.__dict__ for card in objects]
    for obj in objects:
        tmp = dict()
        tmp = obj
        owner = Player.objects.get(id=tmp["owner_id"])
        state = States.objects.get(id=tmp["state_of_card_id"])
        expansion = Expansion.objects.get(id=tmp["set_name_id"])
        colour = Colour.objects.get(id=tmp["colour_id"])
        tmp["owner_id"] = owner.name
        tmp["state_of_card_id"] = state.state
        tmp["set_name_id"] = expansion.name
        tmp["colour_id"] = colour.colour
        items.append(tmp)
    page = request.GET.get('page')
    p = Paginator(items, 25)
    
    cards = p.get_page(page)
    header = ["ID", "Name", "Set", "CMC", "#Karten", "Kartenzustand", "Besitzer", "Farbe/-n"]
    
    logger.warning(header)
    return render(request, 'inventory/index.html', {'header':header, 'rows':cards})