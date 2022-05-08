from django import forms
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"
