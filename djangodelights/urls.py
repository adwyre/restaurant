from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("menu/", views.MenuListView.as_view(), name="menu_list"),
    path("menu/create/", views.MenuCreateView.as_view(), name="menu_create"),
    path("menu/update/<pk>", views.MenuUpdateView.as_view(), name="menu_update"),
    path("menu/delete/<pk>", views.MenuDeleteView.as_view(), name="menu_delete"),
    path("recipe/create/", views.RecipeCreateView.as_view(), name="recipe_create"),
    path("recipe/update/<pk>", views.RecipeUpdateView.as_view(), name="recipe_update"),
    path("recipe/delete/<pk>", views.RecipeDeleteView.as_view(), name="recipe_delete"),
    path("ingredient/", views.IngredientListView.as_view(), name="ingredient_list"),
    path("ingredient/create/", views.IngredientCreateView.as_view(), name="ingredient_create"),
    path("ingredient/update/<pk>", views.IngredientUpdateView.as_view(), name="ingredient_update"),
    path("ingredient/delete/<pk>", views.IngredientDeleteView.as_view(), name="ingredient_delete"),
    path("purchase/", views.PurchaseListView.as_view(), name="purchase_list"),
    path("purchase/create/", views.PurchaseCreateView.as_view(), name="purchase_create"),
]
