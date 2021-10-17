from django.http.response import HttpResponse
from django.shortcuts import render
from wishlist.models import Users, List, Items


# Create your views here.
def index(request):
    return render(request,'wishlist/index.html')

def login(request):
    return render(request,'wishlist/login.html')

def create_account(request):
    return render(request,'wishlist/create_account.html')

def home(request):
    wishlist = [{
            "list_id": "1",
            "user_id": "1",
            "list_name": "Aang Wishlist",
            "slug": "aang-wishlist"
            }, {
            "list_id": "2",
            "user_id": "1",
            "list_name": "Sokka Wishlist",
            "slug": "sokka-wishlist"
            }]
    return render(request,'wishlist/home.html',{'wishlist': wishlist})

def all_items(request):
    return render(request,'wishlist/all_items.html')

def full_list(request, wishlist_slug,user_id):
    wishlist = List.objects.filter(slug=wishlist_slug)
    items = Items.objects.filter(list_id=wishlist[0].list_id)
    print(wishlist[0].list_id)
    print(items[0].name)
    
    return render(request,'wishlist/full_list.html', {"wishlist":wishlist[0], "items":items})

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