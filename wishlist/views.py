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
            request.session['current_list'] = 0
            return redirect('/home/')
    else:        
        return render(request,'wishlist/login.html')

def create_account(request):
    return render(request,'wishlist/create_account.html')

def home(request):
    if request.session['user_id'] > 0:
        wishlist_list = List.objects.filter(user_id = request.session['user_id'])
        request.session['current_list'] = '0'
    else:
        return redirect('/login/')

    return render(request,'wishlist/home.html',{'wishlist': wishlist_list})

def all_items(request):
    return render(request,'wishlist/all_items.html')

def full_list(request):
    if 'current_list' in request.session:
        if request.session['current_list'] != '0':
            wishlist = List.objects.get(list_id=request.session['current_list'])
            items = Items.objects.filter(list_id=request.session['current_list'])
            request.session['current_list'] = '0'
            return render(request,'wishlist/full_list.html', {"wishlist":wishlist, "items":items})
            

    wishlist = List.objects.get(list_id=request.GET.get('list_id'))
    items = Items.objects.filter(list_id=request.GET.get('list_id'))   
    return render(request,'wishlist/full_list.html', {"wishlist":wishlist, "items":items})

def new_list(request):
    wishlist_name = request.POST.get('new_list');
    wishlist_slug = wishlist_name.replace(' ', '-')
    wishlist = List(list_name=wishlist_name,slug=wishlist_slug,user_id=request.session['user_id'])
    wishlist.save()
    return redirect('/home/')

def new_item(request):
    item_name = request.POST.get('new_name')
    item_slug = item_name.replace(' ', '-')
    item_url = request.POST.get('new_url')
    item_description = request.POST.get('new_description')
    item_picture_url = request.POST.get('new_picture_url')
    item_priority = request.POST.get('priority')
    item = Items(name=item_name,url=item_url, description=item_description, picture_url=item_picture_url, user_priority=item_priority, slug=item_slug,user_id=request.session['user_id'], list_id=request.POST.get("list_id") )
    item.save()
    request.session['current_list'] = request.POST.get("list_id")
    return redirect('/items/list/')

def delete_list(request):
#Todo: add confirmation to delete
    list = List.objects.filter(list_id=request.GET.get("list_id"))
    list.delete()
    return redirect('/home/')

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