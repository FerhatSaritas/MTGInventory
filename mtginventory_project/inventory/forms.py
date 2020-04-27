from django import forms
from .models import *
import logging as logger

class CardForm(forms.Form):
    card_name = forms.CharField(label='Name', max_length=100)
    set_name = forms.CharField(label='Set Name', max_length=100)
    cmc = forms.IntegerField(label='CMC')
    num_of_cards = forms.IntegerField(label='#Cards')
    place = forms.CharField(label='Place', max_length=200)
    state_of_card = forms.ChoiceField(choices=(), label='Kartenzustand')
    owner =  forms.ChoiceField(choices=(), label='Spieler')
    colour = forms.ChoiceField(choices=(), label='Colour')

    #img = forms.URLField(max_length=400)

    def __init__(self, *args, **kwargs):
        states = kwargs.pop("states")
        owners = kwargs.pop("owners")
        colours = kwargs.pop("colours")
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['card_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['set_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['cmc'].widget.attrs.update({'class': 'form-control'})
        self.fields['num_of_cards'].widget.attrs.update({'class': 'form-control'})
        self.fields['state_of_card'].widget.attrs.update({'class': 'form-control'})
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['colour'].widget.attrs.update({'class': 'form-control'})
        self.fields['place'].widget.attrs.update({'class': 'form-control'})
        self.fields['state_of_card'].choices = states
        self.fields['owner'].choices = owners
        self.fields['colour'].choices = colours
