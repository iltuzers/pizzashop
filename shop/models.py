from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class FoodManager(models.Manager):
    def get_queryset(self):
        return super(FoodManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['title']),
        ]
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        pass
        #return reverse("shop:category_list", args=[self.slug])


class Food(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='food',
                                 on_delete=models.CASCADE)
    ingredient = models.ManyToManyField("Ingredient", related_name='food', blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to="images/",
                              blank=True) # check this
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)
    objects = models.Manager()
    food_manager = FoodManager()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "food"

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]
        
    def __str__(self):
        return self.name
    


