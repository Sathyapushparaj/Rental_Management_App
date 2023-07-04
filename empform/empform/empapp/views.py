from django.shortcuts import render, redirect
from .form import EmployeeForm
from django.http import HttpResponse



# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if not form.is_valid():
            try:
                return redirect('/')
            except:
                pass
        else:
            form = EmployeeForm()
        return render(request, 'index.html', {'form': form})
