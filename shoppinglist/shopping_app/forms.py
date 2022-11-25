from django import forms
from shopping_app.models import Item, User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
