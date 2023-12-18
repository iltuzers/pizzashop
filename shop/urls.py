from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.food_list, name='food_list'),
    path('menu/<slug:food_slug>/', views.food_detail, name='food_detail'),
    path('<slug:category_slug>/', views.food_by_category, name="food_by_category"),
]


