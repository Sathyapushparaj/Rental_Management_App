from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, "index.html")


def register(request):
    return render(request, "register.html")