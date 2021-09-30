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

# account page using dummy data
def account(request):
    dummyUser = [
        {'firstName': 'Jane',
        'lastName': 'Doe',
        'user_id': '1',
        'username': 'jdoe',
        'password': '12345',
        'admin': 'false'
        }
        
    ]
    return render(request,'wishlist/account.html', {
        'users': dummyUser
    })

# edit account page also using dummy data 
def editAccount(request):
    
    return render(request,'wishlist/editAccount.html')

def item_edit(request):
    return render(request,'wishlist/item_edit.html')