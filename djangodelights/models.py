from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=100)
    unit_price = models.FloatField()

    def get_absolute_url(self):
        return "/ingredient"

    def __str__(self):
        return f"{self.name}"

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def get_absolute_url(self):
        return "/menu"

    def available(self):
        return all(i.enough() for i in RecipeRequirement.objects.filter(menu_item=self.id))

    def __str__(self):
        return f"{self.title}"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def get_absolute_url(self):
        return "/menu"

    def enough(self):
        return self.quantity <= self.ingredient.quantity

    def __str__(self):
        return f"menu_item={self.menu_item.title}; ingredient={self.ingredient.name}; quantity={self.quantity}"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/purchase"

    def revenue(self):
        return self.menu_item.price

    def cost(self):
        total = 0
        reqs = RecipeRequirement.objects.filter(menu_item=self.menu_item.id)
        for req in reqs:
            price = req.quantity * req.ingredient.unit_price
            total += price
        return total

    def profit(self):
        return self.revenue() - self.cost()

    def __str__(self):
        return f"menu_item={self.menu_item.title}; timestamp={self.timestamp}"
