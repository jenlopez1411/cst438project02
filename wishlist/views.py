from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from wishlist.models import Users, List, Items


# Create your views here.
def index(request):
    return render(request,'wishlist/index.html')

def login(request):
    print(request.method)
    if(request.method == 'POST'):
        # print(request.POST.get("uname"))
        # print(request.POST.get("psw"))
        # print(Users.objects.filter(user_name=request.POST.get("uname"), password = request.POST.get("psw")).exists())
        if Users.objects.filter(user_name=request.POST.get("uname"), password = request.POST.get("psw")).exists():
            print(Users.objects.get(user_name=request.POST.get("uname"), password = request.POST.get("psw")).user_id)
            request.session['user_id'] = Users.objects.get(user_name=request.POST.get("uname"), password = request.POST.get("psw")).user_id
            return redirect('/home/')
    else:        
        return render(request,'wishlist/login.html')

def create_account(request):
    return render(request,'wishlist/create_account.html')

def home(request):
    if request.session['user_id'] > 0:
        wishlist_list = List.objects.filter(user_id = request.session['user_id'])
    else:
        return redirect('/login/')

    return render(request,'wishlist/home.html',{'wishlist': wishlist_list})

def all_items(request):
    return render(request,'wishlist/all_items.html')

def full_list(request):
    wishlist = List.objects.get(list_id=request.GET.get('list_id'))
    items = Items.objects.filter(list_id=request.GET.get('list_id'))

    
    return render(request,'wishlist/full_list.html', {"wishlist":wishlist, "items":items})

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

def logout(request):
     request.session['user_id'] = -1;
     return redirect('/login/')