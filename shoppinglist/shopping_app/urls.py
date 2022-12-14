"""shoppinglist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import include, path, re_path
from shopping_app import views

#template tagging
app_name = 'shopping_app'

urlpatterns = [

    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('item_list/', views.ItemListView.as_view(), name='list'),
    path('', views.IndexView.as_view(), name='index'),
    path('item_list/<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('add_item/', views.ItemCreateView.as_view(), name='add'),
    path('edit_item/<int:pk>/', views.ItemUpdateView.as_view(), name='edit'),
    path('delete_item/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),

]
