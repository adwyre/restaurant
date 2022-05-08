from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("menu/list", views.MenuListView.as_view(), name="menu_list"),
    path("menu/create/", views.MenuCreateView.as_view(), name="menu_create"),
    path("menu/update/<pk>", views.MenuUpdateView.as_view(), name="menu_update"),
    path("menu/delete/<pk>", views.MenuDeleteView.as_view(), name="menu_delete"),
]
