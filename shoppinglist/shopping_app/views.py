from django.shortcuts import render
from shopping_app.forms import NewUserForm
from shopping_app.models import User, Item
# Create your views here.

def index(request):
    return render(request, 'shopping_app/index.html')

def test(request):
    return render(request, 'shopping_app/test.html')

def shopping_list(request):
    users = User.objects.order_by('first_name')
    context_dict = {
        'user' : users,
    }
    return render(request, 'shopping_app/shopping_list.html', context=context_dict)

def userform(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return shopping_list(request)
        else:
            print("error-form invalid")

    return render(request, 'shopping_app/user_form.html', {'form':form})