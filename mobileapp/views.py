from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, MobileCreateForm, MobileEditForm, BuyerForm, BuyerEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import Mobile, Buyer


def signin(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("password")
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin')
    return render(request, "mobileapp/login.html")


def registration(request):
    form = UserRegistrationForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("c")
            form.save()
            return redirect('signin')
        else:
            form=UserRegistrationForm(request.POST)
            context["form"]=form
            return render(request, "mobileapp/registration.html", context)

    return render(request, "mobileapp/registration.html", context)




def signout(request):
    logout(request)
    return redirect("home")


def adminpage(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("password")
        if uname == 'vid123' and pwd == 'vidya3979':
            mobile = Mobile.objects.all()
            context = {}
            context['mobile'] = mobile
            return render(request, "mobileapp/base.html")
    return render(request, "mobileapp/adminlogin.html")


def home(request):
    mobilelist = Mobile.objects.all()
    context = {}
    context['mobile'] = mobilelist
    return render(request, "mobileapp/home.html", context)


def add_mobile(request):
    if request.method == "GET":
        mobile = MobileCreateForm()
        context = {}
        context['mobile'] = mobile
        mobilelist = Mobile.objects.all()
        context['mobilelist'] = mobilelist
        return render(request, "mobileapp/addnew_mobile.html", context)
    else:
        mobile = MobileCreateForm(request.POST, request.FILES)
        if mobile.is_valid():
            mobile.save()
            return redirect('add')
        else:
            context = {}
            context['mobile'] = mobile
            mobilelist = Mobile.objects.all()
            context["mobilelist"] = mobilelist
            return render(request, "mobileapp/addnew_mobile.html", context)


def viewMobile(request, id):
    mobile = Mobile.objects.get(id=id)
    context = {}
    context['mobile'] = mobile
    return render(request, 'mobileapp/viewmobile.html', context)


def edit_mobile(request, id):
    if request.method == 'GET':
        mobileid = Mobile.objects.get(id=id)
        mobile = MobileEditForm(instance=mobileid)
        context = {}
        context['mobile'] = mobile
        return render(request, 'mobileapp/edit_mobile.html', context)
    else:
        mobileid = Mobile.objects.get(id=id)
        mobile = MobileEditForm(request.POST, request.FILES, instance=mobileid)
        if mobile.is_valid():
            mobile.save()
            return render(request,'mobileapp/base.html')


def delete_mobile(request, id):
    Mobile.objects.get(id=id).delete()
    return render(request,'mobileapp/base.html')


def search_mobile(request):
    if request.method == 'GET':
        return render(request, 'mobileapp/search.html')
    if request.method == 'POST':
        item = str(request.POST.get('item'))
        mobilelist = Mobile.objects.filter(Q(mobile_name__iexact=item) | Q(manufacturer__iexact=item))
        context = {}
        context['mobile'] = mobilelist
        context['item'] = item
        return render(request, 'mobileapp/home.html', context)


def sort_mobile(request):
    if request.method == "GET":
        return render(request, 'mobileapp/sort.html')
    if request.method == 'POST':
        min_price = request.POST.get('price1')
        max_price = request.POST.get('price2')
        mobilelist = Mobile.objects.filter(price__gte=min_price, price__lte=max_price)
        context = {}
        context['mobile'] = mobilelist
        context['item'] = [min_price, max_price]
        return render(request, 'mobileapp/home.html', context)

@login_required
def buyer_details(request, id):
    product = Mobile.objects.get(id=id).model_number
    form = BuyerForm(initial={'product': product, 'user': request.user})
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['form'] = form
            return render(request, 'mobileapp/buyerdetail.html', context)
    return render(request, 'mobileapp/buyerdetail.html', context)


def viewOrder(request):
    if request.method == "GET":
        orders = Buyer.objects.all()
        if Buyer.objects.last().status == None:
            obj1 = Buyer.objects.last()
            obj1.status = "NO"
            obj1.save()
        context = {}

        context['orders'] = orders

        return render(request, 'mobileapp/vieworder.html', context)


def editorder(request, id):
    if request.method == 'GET':
        orders = Buyer.objects.get(id=id)
        form = BuyerEditForm(instance=orders)
        context = {}
        context['form'] = form
        return render(request, 'mobileapp/editorder.html', context)
    else:
        orders = Buyer.objects.get(id=id)
        form = BuyerEditForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('vieworder')

def cancelorder(request,id):
    Buyer.objects.get(id=id).delete()
    return redirect('vieworder')
