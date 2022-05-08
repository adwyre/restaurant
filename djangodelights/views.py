from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import MenuForm
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
        context["reqs"] = RecipeRequirement.objects.all()
        context["ingredients"] = Ingredient.objects.all()
        return context
class MenuCreateView(CreateView):
    model = MenuItem
    template_name = "djangodelights/menu_create.html"
    form_class = MenuForm
class MenuUpdateView(UpdateView):
    model = MenuItem
    template_name = "djangodelights/menu_update.html"
    form_class = MenuForm
class MenuDeleteView(DeleteView):
    model = MenuItem
    template_name = "djangodelights/menu_delete.html"
    form_class = MenuForm
    success_url = "menu_list"
