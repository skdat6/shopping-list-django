from django.contrib import admin
from shopping_app.models import User, Item, UserProfileInfo

# Register your models here.
admin.site.register(Item)
admin.site.register(UserProfileInfo)