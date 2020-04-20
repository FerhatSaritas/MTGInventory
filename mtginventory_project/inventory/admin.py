from django.contrib import admin
from .models import Expansion, Colour, States, Card, Player
# Register your models here.

admin.site.register(Expansion)
admin.site.register(States)
admin.site.register(Colour)
admin.site.register(Player)
admin.site.register(Card)