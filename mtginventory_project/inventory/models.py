from django.db import models

# Create your models here.
class Expansion(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class States(models.Model):
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.state

class Player(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Colour(models.Model):
    colour = models.CharField(max_length=100)

    def __str__(self):
        return self.colour

class Card(models.Model):
    name = models.CharField(max_length=400)
    set_name = models.ForeignKey(Expansion, on_delete=models.CASCADE)
    cmc = models.IntegerField()
    num_of_cards = models.IntegerField()
    state_of_card = models.ForeignKey(States, on_delete=models.CASCADE)
    owner =  models.ForeignKey(Player, on_delete=models.CASCADE)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    img = models.URLField(max_length=400)

    def __str__(self):
        return self.name + ' - '+ str(self.set_name)
