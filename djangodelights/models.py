from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    CUPS = 'CUPS'
    POUNDS = 'LBS'
    TABLESPOONS = 'TBSP'
    TEASPOONS = 'TSP'
    OUNCES = 'OZ'
    GRAMS = 'GS'
    EGGS = 'EGGS'
    UNITS=[
        (CUPS, 'cups'),
        (POUNDS, 'lbs'),
        (TABLESPOONS, 'tbsp'),
        (TEASPOONS, 'tsp'),
        (OUNCES, 'ounces'),
        (GRAMS, 'grams'),
        (EGGS, 'eggs')
    ]
    unit = models.CharField(max_length=4, choices=UNITS, default=CUPS)
    unit_price = models.FloatField()

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
