from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
# Create your views here.
class IndexView(TemplateView):
    template_name = "djangodelights/index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["ingredients"] = Ingredient.objects.all()
        context["menuitems"] = MenuItem.objects.all()
        context["reqs"] = RecipeRequirement.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

class MenuListView(ListView):
    model = MenuItem
    template_name = "djangodelights/menu_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["menuitems"] = MenuItem.objects.all()
        return context
