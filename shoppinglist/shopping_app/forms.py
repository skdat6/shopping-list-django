from django import forms
from django.contrib.auth.models import User
from shopping_app.models import Item, User, UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('favorite_shopping_site', 'profile_pic')


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name', 'category', 'price')

