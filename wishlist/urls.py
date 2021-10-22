from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name='landing-index'),
    path('login/', views.login, name='login'),
    path('create-account/', views.create_account, name ='create-account'),
    path('home/', views.home, name='home'),
    path('items/', views.all_items, name='items'),
    path('items/list/', views.full_list, name='full-list'),
    path('account/', views.account, name='account'),
    path('items/edit/', views.item_edit, name='item-edit'),
    path('items/list/edit/', views.item_edit, name='item-edit'),
    path('edit/', views.item_edit, name='item-edit'),
    path('editAccount/', views.editAccount, name = 'editAccount'),
    path('logout/', views.logout, name='logout'),
    path('new-list/',views.new_list, name='new-list'),
    path('new-item/',views.new_item, name='new-item'),
    path('delete-list', views.delete_list, name='delete-list')
]