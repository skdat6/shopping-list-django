from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from shopping_app.models import User, Item, User
from shopping_app.forms import UserForm, UserProfileInfoForm
# Create your views here.

#CREATE ITEM VIEW
class ItemCreateView(CreateView):
    model = models.Item
    fields = ('item_name', 'category', 'price')

#UPDATE ITEM VIEW
class ItemUpdateView(UpdateView):
    model = models.Item
    fields = ('item_name', 'category', 'price')

#DELETE ITEM VIEW
class ItemDeleteView(DeleteView):
    model = models.Item
    success_url = reverse_lazy("shopping_app:list")


class ItemListView(ListView):
    model = models.Item


class ItemDetailView(DetailView):
    context_object_name = "item_detail"
    model = models.Item
    template_name = "shopping_app/item_detail.html"


class IndexView(TemplateView):
    template_name = 'shopping_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context


# def index(request):
#     context_dict = {'text' : 'hello ppl',
#                     'number':100
#                     }
#     return render(request, 'shopping_app/index.html', context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'shopping_app/index.html', {})


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'shopping_app/register.html', {'user_form': user_form,
                                                          'profile_form': profile_form,
                                                          'registered': registered})



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'shopping_app/shopping_list.html', {})


            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone failed a login attempt")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'shopping_app/login.html', {})

    return render(request, 'shopping_app/login.html', {})

@login_required
def shopping_list(request):
    users = User.objects.order_by('first_name')
    context_dict = {
        'user' : users,
    }
    return render(request, 'shopping_app/shopping_list.html', context=context_dict)

