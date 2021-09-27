from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'wishlist/index.html')

def login(request):
    return render(request,'wishlist/login.html')

def create_account(request):
    return render(request,'wishlist/create_account.html')

def home(request):
    return render(request,'wishlist/home.html')

def all_items(request):
    return render(request,'wishlist/all_items.html')

def full_list(request):
    return render(request,'wishlist/full_list.html')

def account(request):
    return render(request,'wishlist/account.html')

def item_edit(request):
    return render(request,'wishlist/item_edit.html')

       