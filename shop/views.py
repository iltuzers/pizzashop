from django.shortcuts import render, get_object_or_404
from .models import Category, Food, Ingredient

def index(request):
    """ Display num_food food in the home page randomly """
    random_food_list = Food.random_manager.all()[:6]
    context = {"random_food_list": random_food_list }
    return render(request, "shop/index.html", context=context)

def food_list(request):
    food_all = Food.food_manager.all()
    return render(request, "shop/food/menu.html", {'food_all': food_all})


def food_by_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    category_food = Food.food_manager.filter(category=category)
    return render(request, "shop/food/food_by_category.html", {"category_food": category_food, "category": category })

def food_detail(request, food_slug):
    food = get_object_or_404(Food, slug=food_slug)
    return render(request, "shop/food/food_detail.html", {"food": food})
