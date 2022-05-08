from django import forms
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from django.forms import Select

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['menu_item',]
