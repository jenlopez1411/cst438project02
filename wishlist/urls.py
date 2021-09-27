from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name='landing-index'),
    path('login/', views.login, name='login'),
    path('create-account/', views.create_account, name ='create-account'),
    path('home/', views.home, name='home'),
    path('items', views.all_items, name='items'),
    path('items/list', views.full_list, name='full-list'),
    path('account/', views.account, name='account'),
    path('item/edit/', views.item_edit, name='item-edit')

]