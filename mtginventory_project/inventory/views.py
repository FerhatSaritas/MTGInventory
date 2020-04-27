from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Card, Player, States, Colour, Expansion
from .forms import CardForm
import logging as logger
# Create your views here.

def index(request):
    if request.method == 'POST':
        # Chekc if request is a POST action
        states, owners, colours = getObjects()
        form = CardForm(request.POST, states=states, owners=owners, colours=colours)
        if form.is_valid():
            # Read data from the request and store it as a new entry in db
             card_name = form.cleaned_data['card_name']
             if Expansion.objects.filter(name=form.cleaned_data['set_name']).first():
                 # Check if the expansion already is in the DB
                 set_name = Expansion.objects.get(name=form.cleaned_data['set_name'])
             else:
                 set_name = Expansion(name=form.cleaned_data['set_name'])
             set_name.save()
             cmc = form.cleaned_data['cmc']
             num_of_cards = form.cleaned_data['num_of_cards']
             state_of_card = States.objects.get(id=form.cleaned_data['state_of_card'])
             owner = Player.objects.get(id=form.cleaned_data['owner'])
             colour = Colour.objects.get(id=form.cleaned_data['colour'])
             place = form.cleaned_data['place']
             if Card.objects.filter(name=card_name, set_name=set_name, cmc=cmc, num_of_cards=num_of_cards, state_of_card=state_of_card, owner=owner, colour=colour, place=place).first():
                 # Check if a card with same properties already is in DB
                 logger.warning(forms.ValidationError('This entry already exists'))
             else:
                new_card = Card(name=card_name, set_name=set_name, cmc=cmc, num_of_cards=num_of_cards, state_of_card=state_of_card, owner=owner, colour=colour, img='', place=place)
                new_card.save()

    states, owners, colours = getObjects()
    new_form = CardForm(states=states, owners=owners, colours=colours)
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
    header = ["Name", "Set", "CMC", "#Karten", "Plan?", "Besitzer", "Farbe/-n", "Wo?"]
    
    context = {
        'header':header, 
        'rows':cards, 
        'form':new_form
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