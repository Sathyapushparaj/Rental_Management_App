from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import requires_csrf_token


def home(request):
    test = House.objects.all()
    return render(request, "index.html", {"test": test})


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
        return redirect('main')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                return redirect("/")

            else:
                messages.error(request, "Invalid User Name or Password")
                return redirect("loginpage")
        return render(request, "loginpage.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Success You Can Login Now...! ")
            return redirect('/loginpage')
    else:
        form = CustomUserForm()
    return render(request, "register.html", {'form': form})


@login_required
@requires_csrf_token
def appartment(request):
    House = request.GET.get('House')

    if House == None:
        product = Add_place.objects.order_by('-name').filter(is_published=True)

    else:
        product = Add_place.objects.filter(house__name=House)

    return render(request, "appart.html", {"product": product})


@login_required
def productdetails(request, pk):
    eachproduct = Add_place.objects.get(name=pk)

    return render(request, "products.html", {"eachproduct": eachproduct})

@login_required
def searchBar(request):

    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            product = Add_place.objects.filter(name__icontains=query)
            return render(request, 'searchbar.html', {'product': product})

        else:
            print("No information Show")
            return render(request, 'searchbar.html', {})



def aboutpage(request):
    return render(request, 'about.html')


def dialpadpage(request):
    return render(request, 'dialpad.html')

