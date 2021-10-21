from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from wishlist.models import Users


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST
        print(name["name"])
        print(name["username"])
        print(name["password"])
        print(name["password-repeat"])
        if name["password"] == name["password-repeat"]:
            Users.objects.create(first_name = name["name"], user_name = name["username"], password = name["password"])
        else: 
            print("error mess")
            messages.error(request, 'Password does not match')
    return render(request,'wishlist/index.html')

def login(request):
    if request.method == 'POST':
        user = request.POST
        users = Users.objects.all()
        for u in users.iterator():
            if user["username"] == u.user_name:
                print(user["username"] + " match")
                return render(request, 'wishlist/home.html', {'userID': u.user_id})
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

def full_list(request, wishlist_slug):
    wishlists = [{
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
    items = [{
            "user_id": "1",
            "list_id": "1",
            "item_id": "1",
            "name": "Appa Stuffed",
            "url": "https://amzn.to/39Im8cz",
            "description": "This is a stuffed Appa",
            "picture": "https://i.imgur.com/HT9YCFB.png",
            "user_priority": "high",
            "slug": "stuffed-appa"
            },
            {
            "user_id": "1",
            "list_id": "2",
            "item_id": "2",
            "name": "Momo Stuffed",
            "url": "https://amzn.to/2WkXR9q",
            "description": "This is a stuffed Momo",
            "picture": "https://imgur.com/fQe01dl",
            "user_priority": "high",
            "slug": "stuffed-momo",
            },
            {
            "user_id": "1",
            "list_id": "2",
            "item_id": "3",
            "name": "Momo Stuffed 2",
            "url": "https://amzn.to/2WkXR9q",
            "description": "This is a stuffed Momo 2",
            "picture": "https://imgur.com/fQe01dl",
            "user_priority": "high",
            "slug": "stuffed-momo-2"
            }
            

      ]
    current_list = []
    print("slug = ")
    print(wishlist_slug)
    for wishlist in wishlists:
        print(wishlist["slug"])
        print(wishlist["slug"] == wishlist_slug)
        if wishlist["slug"] == wishlist_slug:
            current_list.append(wishlist.copy())
            break;
    print("got list")
    print(current_list)        
    current_items = []
    for item in items:
        print(item)
        print(item["list_id"])
        
        if item["list_id"] == current_list[0]["list_id"]:
            current_items.append(item)
    print(current_list)
    print(current_items)

    return render(request,'wishlist/full_list.html', {"wishlist":current_list[0], "items":current_items })

# account page using dummy data
def account(request):
    print("hello there")
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