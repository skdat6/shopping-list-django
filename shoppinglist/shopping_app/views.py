from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from shopping_app.models import User, Item, User
from shopping_app.forms import UserForm, UserProfileInfoForm


# CREATE ITEM VIEW
class ItemCreateView(LoginRequiredMixin, CreateView):
    success_url = '/item_list/'

    model = models.Item
    fields = ('item_name', 'category', 'price')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# UPDATE ITEM VIEW
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Item
    fields = ('item_name', 'category', 'price')


# DELETE ITEM VIEW
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Item
    success_url = reverse_lazy("shopping_app:list")


class ItemListView(LoginRequiredMixin, ListView):
    model = models.Item

    def get_queryset(self):
        return Item.objects.all()


class ItemDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "item_detail"
    model = models.Item
    template_name = "shopping_app/item_detail.html"


class IndexView(TemplateView):
    template_name = 'shopping_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context


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
                return HttpResponseRedirect(reverse("list"))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone failed a login attempt")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'shopping_app/login.html', {})

    return render(request, 'shopping_app/item_list.html', {})


@login_required
def shopping_list(request):
    users = User.objects.order_by('first_name')
    context_dict = {
        'user': users,
    }
    return render(request, 'shopping_app/shopping_list.html', context=context_dict)

