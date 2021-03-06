from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from wishlist.models import Users, List, Items
from .forms import UserForm

# Create your views here.
def index(request):
    request.session['user_id'] = 0
    request.session['admin'] = 0 
    if 'login_fail' not in request.session:
        request.session['login_fail'] = 0 
    if request.session['login_fail'] == 0:  
        return render(request,'wishlist/index.html', {'message' : ""})
    elif request.session['login_fail'] == 1:
        request.session['login_fail'] = 0 
        return render(request,'wishlist/index.html', {'message' : "Username/Password is wrong."})
    else:
        request.session['login_fail'] = 0 
        return render(request,'wishlist/index.html', {'message' : "Similar user created, please sign up again"})


def login(request):
    if request.method == 'POST':
        user = request.POST
        # users = Users.objects.all()
        # for u in users.iterator():
        #     if user["uname"] == u.user_name and user["psw"] == u.password:
        #         print(user["uname"] + " match")
        
        if Users.objects.filter(user_name=request.POST.get("uname"), password = request.POST.get("psw")).exists():
                # return render(request, 'wishlist/home.html', {'userID': u.user_id})
                u = Users.objects.get(user_name=request.POST.get("uname"), password = request.POST.get("psw"))
                request.session['user_id'] = u.user_id                
                request.session['current_list'] = 0
                request.session['login_fail'] = 0
                if u.user_name != 'admin': 
                    return redirect('/home/')
                else:
                    request.session['admin'] = 1
                    request.session['login_fail'] = 0
                    return redirect('/new_admin/')
        else:
                request.session['login_fail'] = 1
                return redirect('/')
             
    else:
        return render(request,'wishlist/index.html')

def create_account(request):
    if request.method == 'POST':
        name = request.POST
        if Users.objects.filter(user_name=request.POST.get("uname")).exists():
            print("error exists")
            request.session['login_fail'] = 2
            return redirect('/')
        else:
            if name["psw"] == name["psw-repeat"]:
                Users.objects.create(first_name = name["name"], user_name = name["uname"], password = name["psw"])
                print("pasa")
            else: 
                print("error create acc")
                #return render( request, 'wishlist/create_account.html', {'message': "Password does not match."})
                return redirect('create-account', message = "Password does not match.")
    return redirect('/')

def home(request):
    if request.session['user_id'] > 0:
        wishlist_list = List.objects.filter(user_id = request.session['user_id'])
        request.session['current_list'] = '0'
    else:
        return redirect('/')

    return render(request,'wishlist/home.html',{'wishlist': wishlist_list})

def all_items(request):
    if request.session['user_id'] == 0:
        return redirect('/')
    items = Items.objects.filter(user_id = request.session['user_id'])
    if 'current_list' in request.session:
        request.session['current_list'] = '0'
    return render(request,'wishlist/all_items.html', {"items": items})

def full_list(request):
    if request.session['user_id'] == 0:
        return redirect('/')
    if 'current_list' in request.session:
        if request.session['current_list'] != '0':
            wishlist = List.objects.get(list_id=request.session['current_list'])
            items = Items.objects.filter(list_id=request.session['current_list'])
            #request.session['current_list'] = '0'
            return render(request,'wishlist/full_list.html', {"wishlist":wishlist, "items":items})
            

    wishlist = List.objects.get(list_id=request.GET.get('list_id'))
    items = Items.objects.filter(list_id=request.GET.get('list_id'))   
    return render(request,'wishlist/full_list.html', {"wishlist":wishlist, "items":items})

def new_list(request):
    wishlist_name = request.POST.get('new_list');
    wishlist = List(list_name=wishlist_name,user_id=request.session['user_id'])
    wishlist.save()
    return redirect('/home/')

def new_item(request):
    item_name = request.POST.get('new_name')
    item_url = request.POST.get('new_url')
    item_description = request.POST.get('new_description')
    item_picture_url = request.POST.get('new_picture_url')
    item_priority = request.POST.get('priority')
    item = Items(name=item_name,url=item_url, description=item_description, picture_url=item_picture_url, user_priority=item_priority,user_id=request.session['user_id'], list_id=request.POST.get("list_id") )
    item.save()
    if 'current_list' in request.session and request.POST.get("list_id")!= "0" :
     request.session['current_list'] = request.POST.get("list_id")
     return redirect('/items/list/')
    return redirect('/items/')

def delete_list(request):
#Todo: add confirmation to delete
    list = List.objects.filter(list_id=request.GET.get("list_id"))
    list.delete()
    return redirect('/home/')

# account
def account(request):
    if request.session['user_id'] == 0:
        return redirect('/')
    user_id = request.session['user_id']
    users = Users.objects.all()
    for u in users.iterator():
        if user_id == u.user_id:
            firstName = u.first_name
            userName = u.user_name
            # user_id = u.user_id
            return render(request, 'wishlist/account.html', {
                  'fname' : firstName,
                  'userName': userName,
                  'user_id' : user_id
                  })

# edit account page also using dummy data 
def new_admin(request):
    if request.session['user_id'] == 0:
        return redirect('/')
    if request.session['admin'] == 0:
        return redirect('/home/') 
    users = Users.objects.all()
    return render(request,'wishlist/new_admin.html',{'users':users})

def delete_user(request):
#Todo: add confirmation to delete
    user = Users.objects.filter(user_id=request.POST.get("user_id"))
    user.delete()
    return redirect('/new_admin/')
def create_user_admin(request):
    first_name = request.POST.get('first_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = Users(first_name=first_name,user_name=username, password=password)
    user.save()
    return redirect('/new_admin/')

def edit_user_admin(request):
    user = Users.objects.get(user_id=request.POST.get('user_id'))
    user.first_name = request.POST.get('first_name')
    user.user_name = request.POST.get('username')
    user.password = request.POST.get('password')
    user.save()
    return redirect('/new_admin/')
    
def editAccount(request, user_id):
    if request.session['user_id'] == 0:
        return redirect('/') 
    user_id = request.session['user_id']
    users = Users.objects.all()
    for u in users.iterator():
        if user_id == u.user_id:
            user = Users.objects.get(user_id = user_id)
            form = UserForm(instance=user)
            if request.method == 'POST':
                form = UserForm(request.POST, instance = user)
                if(form.is_valid):
                    form.save()
                    return redirect('/account')
            # return redirect('/')
                
            context = {'form': form}
            return render(request,'wishlist/editAccount.html', context)

def item_edit(request):
    item = Items.objects.get(item_id=request.GET.get('item_id'))
    return render(request,'wishlist/item_edit.html', {"item":item})

def edit_item(request):
    item = Items.objects.get(item_id=request.POST.get('item_id'))
    item.name = request.POST.get('itemname')
    item.url = request.POST.get('url')
    item.description = request.POST.get('description')
    item.picture_url = request.POST.get('pictureurl')
    item.save()

    if 'current_list' in request.session and request.session.get("list_id")!= "0" :
     request.session['current_list'] = item.list_id
     return redirect('/items/list/')
    return redirect('/items/')


def logout(request):
     request.session['user_id'] = 0
     request.session['admin'] = 0
     request.session['login_fail'] = 0 
     return redirect('/')