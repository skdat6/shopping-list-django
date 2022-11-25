from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=264)

    class ItemCategories(models.TextChoices):
        VEGETABLES = 'Vegetables'
        FRUIT = 'Fruit'
        MEAT = 'Meat'
        DRINKS = 'Drinks'
        SNACKS = 'Snacks'
        DAIRY = 'Dairy'
        PET = 'Pet'
        SKINCARE = 'Skin Care'
        HAIR = 'Hair Products'
        AUTO = 'Auto-vehicle'
        ELECTRONICS = 'Electronics'

    category = models.CharField(choices=ItemCategories.choices, max_length=264)
    price = models.FloatField()

    def __str__(self):
        return self.item_name
