from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Card, Player, States, Colour, Expansion
from .forms import CardForm
import logging as logger
# Create your views here.

def index(request):
    states, owners, colours = getObjects()
    if request.method == 'POST':
        form = CardForm(request.POST, states=states, owners=owners, colours=colours)
        if form.is_valid():
            # Der neue Eintrag wird gespeichert
            logger.warning(request.POST)
    
    form = CardForm(states=states, owners=owners, colours=colours)
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
    
    context = {
        'header':header, 
        'rows':cards, 
        'form':form
        }
    return render(request=request, template_name='inventory/index.html', context=context)


def getObjects():
    states = States.objects.all()
    states = ((state.__dict__['id'],state.__dict__['state']) for state in states)
    
    owners = Player.objects.all()
    owners = ((owner.__dict__['id'], owner.__dict__['name']) for owner in owners)

    colours = Colour.objects.all()
    colours = ((colour.__dict__['id'], colour.__dict__['colour']) for colour in colours)

    return [states, owners, colours]