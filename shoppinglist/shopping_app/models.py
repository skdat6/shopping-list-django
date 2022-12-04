from django.db import models
from django.contrib.auth.models import User
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
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.item_name


# class User(models.Model):
#     first_name = models.CharField(max_length=264)
#     last_name = models.CharField(max_length=264)
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         return str(self.first_name)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #aditional
    favorite_shopping_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    items = models.OneToOneField(Item, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username