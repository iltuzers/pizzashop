from django.contrib import admin
from .models import Category, Food, Ingredient


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "available"]
    list_filter = ["available"]
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug": ("name", )}

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name"]
