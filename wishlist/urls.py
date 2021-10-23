from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name='landing-index'),
    path('login/', views.login, name='login'),
    path('create-account/', views.create_account, name ='create-account'),
    path('home/', views.home, name='home'),
    path('items/', views.all_items, name='items'),
    path('items/list/', views.full_list, name='full-list'),
    path('account/{user_id}/', views.account, name='account'),
    path('account/', views.account, name='account'),
    path('item/edit/', views.item_edit, name='item-edit'),
    path('editAccount/<user_id>', views.editAccount, name = 'editAccount'),
    path('logout/', views.logout, name='logout'),
    path('new-list/',views.new_list, name='new-list'),
    path('new-item/',views.new_item, name='new-item'),
    path('delete-list', views.delete_list, name='delete-list'),
    path('new_admin', views.new_admin, name = "new_admin"),
    path('delete-user/', views.delete_user, name='delete-user'),
    path('new_admin/', views.new_admin, name = "new_admin"),
    path('new_user_admin/', views.create_user_admin, name = "new-user-admin"), 
    path('edit_user_admin/', views.edit_user_admin, name = "edit-user-admin")
]