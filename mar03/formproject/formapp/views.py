from django.shortcuts import render,redirect
from .forms import Employee
from .models import Employee



# Create your views here.

def home(request):
    mydata = Employee.objects.all()
    if (mydata != ''):

        return render(request, "index.html", {'datas': mydata})
    else:
        return render(request, "index.html")

def addData(request):
    if request.method== "POST":
        eid=request.POST["eid"]
        ename = request.POST["ename"]
        econtact = request.POST["econtact"]
        address = request.POST["address"]

        obj=Employee();
        obj.eid= eid
        obj.ename = ename
        obj.econtact = econtact
        obj.address = address

        obj.save()
        mydata = Employee.objects.all()
        return render(request,"index.html", {'datas': mydata})
    return render(request, "index.html")

def updateData(request, id):
    mydata = Employee.objects.get(id=id)
    if request.method == "POST":
        eid = request.POST['eid']
        ename = request.POST['ename']
        econtact = request.POST['econtact']
        address = request.POST['address']

        mydata.eid = eid
        mydata.ename = ename
        mydata.econtact = econtact
        mydata.address = address
        mydata.save()
        return redirect('home')
    return render(request, "update.html", {'data': mydata})

def deleteData(request, id):
    mydata = Employee.objects.get(id=id)
    mydata.delete()
    return redirect('home')
