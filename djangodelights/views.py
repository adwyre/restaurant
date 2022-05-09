from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import MenuForm, RecipeForm, IngredientForm, PurchaseForm
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
    success_url = "/menu"

class RecipeCreateView(CreateView):
    model = RecipeRequirement
    template_name = "djangodelights/recipe_create.html"
    form_class = RecipeForm
class RecipeUpdateView(UpdateView):
    model = RecipeRequirement
    template_name = "djangodelights/recipe_update.html"
    form_class = RecipeForm
class RecipeDeleteView(DeleteView):
    model = RecipeRequirement
    template_name = "djangodelights/recipe_delete.html"
    success_url = "/menu"

class IngredientListView(ListView):
    model = Ingredient
    template_name = "djangodelights/ingredient_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["ingredients"] = Ingredient.objects.all()
        return context
class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "djangodelights/ingredient_create.html"
    form_class = IngredientForm
class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "djangodelights/ingredient_update.html"
    form_class = IngredientForm
class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "djangodelights/ingredient_delete.html"
    success_url = "/ingredient"

class PurchaseListView(ListView):
    model = Purchase
    template_name = "djangodelights/purchase_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["purchases"] = Purchase.objects.all()
        return context
class PurchaseCreateView(TemplateView):
    model = Purchase
    template_name = "djangodelights/purchase_create.html"
    form_class = PurchaseForm

    def get_context_data(self):
        context = super().get_context_data()
        context["menu_items"] = [item for item in MenuItem.objects.all() if item.available()]
        return context

    def post(self, request):
        menu_item_title = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(title=menu_item_title)
        reqs = RecipeRequirement.objects.filter(menu_item=menu_item)
        purchase = Purchase(menu_item=menu_item)
        # Update ingredient quantity in inventory
        for req in reqs:
            req.ingredient.quantity -= req.quantity
            req.ingredient.save()
        purchase.save()
        return redirect("/purchase")

class ReportView(TemplateView):
    template_name = "djangodelights/report.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["purchases"] = Purchase.objects.all()
        context["revenues"] = [purchase.revenue() for purchase in Purchase.objects.all()]
        context["costs"] = [purchase.cost() for purchase in Purchase.objects.all()]
        context["profit"] = sum([purchase.profit() for purchase in Purchase.objects.all()])
        return context
