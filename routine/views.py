from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Department,Task,Service
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, timedelta, time


def index(request):
    return HttpResponse("<h1> Welcome </h1> ")

def departments(request):
    user=request.user
    if user.is_authenticated():
        depts=[user.userprofile.department]
    else:
        depts = Department.objects.all()
    return render(request, "departments.html", {"departments": depts})


def tasks(request):
    task = Task.objects.all()
    return render(request, "tasks.html", {"tasks": task })

def user_login(request):
    if request.method == "GET":
        return render(request,"login.html")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print username
        print password
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            #import ipdb;ipdb.set_trace()
            if user.userprofile.department.name=="Audio":
                return HttpResponseRedirect("/routine/audio/")
                return render(request, "login_success.html")
            elif user.userprofile.department.name=="Media":
                return HttpResponseRedirect("/routine/media/")
                return render(request,"login_success.html")
            elif user.userprofile.department.name=="Lights":
                return HttpResponseRedirect("/routine/light/")
                return render(request, "login_success.html")
            elif user.userprofile.department.name == "Stage":
                return HttpResponseRedirect("/routine/stage/")
                return render(request, "login_sucess.html")
            elif user.userprofile.department.name == "Power":
                return HttpResponseRedirect("/routine/power/")
                return render(request, "login_sucess.html")
            elif user.userprofile.department.name == "Inventory":
                return HttpResponseRedirect("/routine/inventory/")
                return render(request, "login_sucess.html")
            elif user.userprofile.department.name == "Truss":
                return HttpResponseRedirect("/routine/truss/")
                return render(request, "login_sucess.html")

        else:
            return render(request, "login.html",{"failed":True})



def user_logout(request):
    user = request.user
    if user.is_authenticated():
        logout(request)
        return HttpResponse("<h1> logout sucessfully </h1>")
    else:
        return HttpResponse("<h1> user not loged in </h1>")


def audio(request):
    if request.method == "GET":
        return render(request,"audio.html")
    if request.method == "POST":
        #task=request.POST[""]
        service_name = request.POST["service"]
        user = request.user
        dept = user.userprofile.department
        task1_name = "Line Check" if request.POST.get("LineTask", "") else ""
        task2_name = "Sound Check" if request.POST.get("SoundTask", "") else ""
        task3_name = "Change over" if request.POST.get("ChangeTask", "") else ""
        if dept.name=="Audio":
            task1 = Task.objects.filter(name=task1_name,department=dept).first()
            task2 = Task.objects.filter(name=task2_name,department=dept).first()
            task3 = Task.objects.filter(name=task3_name,department=dept).first()
            if task1:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task1
                service.complete = True
                service.date = datetime.now()
                service.save()
            if task2:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task2
                service.complete = True
                service.date = datetime.now()
                service.save()
            if task3:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task3
                service.complete = True
                service.date = datetime.now()
                service.save()
            return HttpResponse("saved")
        return HttpResponse("not valid")


def media(request):
    if request.method == "GET":
        return render(request,"media.html")
    if request.method == "POST":
        service_name = request.POST["service"]

        user = request.user
        dept = user.userprofile.department

        task1_name = "Select Background" if request.POST.get("BackgroundTask", " ")else ""
        task2_name = "Lyrics" if request.POST.get("LyricsTask", " ")else ""
        task3_name = "News" if request.POST.get("NewsTask", " ")else""
        task4_name = "PPTS" if request.POST.get("PPTSTask", " ") else""

        if dept.name=="Media":
            task1 = Task.objects.filter(name=task1_name,department=dept).first()
            task2 = Task.objects.filter(name=task2_name,department=dept).first()
            task3 = Task.objects.filter(name=task3_name,department=dept).first()
            task4 = Task.objects.filter(name=task4_name,department=dept).first()
            if task1:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task1
                service.complete = True
                service.date = datetime.now()
                service.save()
            if task2:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task2
                service.complete = True
                service.date = datetime.now()
                service.save()

            if task3:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task3
                service.complete = True
                service.date = datetime.now()
                service.save()

            if task4:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task4
                service.complete = True
                service.date = datetime.now()
                service.save()


            return HttpResponse("saved")
        return HttpResponse("not valid")



def light(request):
    if request.method == "GET":
        return render(request,"light.html")
    if request.method == "POST":
        service_name = request.POST["service"]

        user = request.user
        dept = user.userprofile.department

        task1_name ="Program Cues For Songs" if request.POST.get("CuesTask", " ") else""
        task2_name = "Hall Lights Manage" if request.POST.get("HallTask", " ") else""
        task3_name = "Change over" if request.POST.get("ChangeoverTask", " ") else""

        if dept.name == "Lights":
            task1 = Task.objects.filter(name=task1_name,department=dept).first()
            task2 = Task.objects.filter(name=task2_name,department=dept).first()
            task3 = Task.objects.filter(name=task3_name,department=dept).first()

            if task1:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task1
                service.complete = True
                service.date = datetime.now()
                service.save()

            if task2:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task2
                service.complete = True
                service.date = datetime.now()
                service.save()

            if task3:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task3
                service.complete = True
                service.date = datetime.now()
                service.save()


            return HttpResponse("saved")
        return HttpResponse("not valid")

def stage(request):
    if request.method=="GET":
        return render(request,"stage.html")
    if request.method == "POST":
        service_name = request.POST["service"]

        user = request.user
        dept = user.userprofile.department

        task1_name = "Set Up Stage For Line Check" if request.POST.get("SetupTask", " ") else""
        task2_name =" Swap Batteries"  if request.POST.get("SwapTask", " ") else""
        task3_name ="Trouble Shoots" if request.POST.get("ShootsTask", " ")else""

        if dept.name == "Stage":
            task1 = Task.objects.filter(name=task1_name,department=dept).first()
            task2 = Task.objects.filter(name=task2_name,department=dept).first()
            task3 = Task.objects.filter(name=task3_name,department=dept).first()

            if task1:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task1
                service.complete = True
                service.date = datetime.now()
                service.save()
            if task2:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task2
                service.complete = True
                service.date = datetime.now()
                service.save()
            if task3:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task3
                service.complete = True
                service.date = datetime.now()
                service.save()

            return HttpResponse("saved")
        return HttpResponse("not valid")


def power(request):
    if request.method =="GET":
        return render(request,"power.html")
    if request.method == "POST":
        service_name = request.POST["service"]

        user = request.user
        dept = user.userprofile.department
        task1_name ="Check Voltage At Different Power Points" if request.POST.get("VoltageTask", " ") else""
        task2_name = "A/c's" if request.POST.get("AcTask", " ") else""
        task3_name = "Generator" if request.POST.get("GeneratorTask", " ") else""

        if dept.name == "Power":
            task1 = Task.objects.filter(name=task1_name,department=dept).first()
            task2 = Task.objects.filter(name=task2_name,department=dept).first()
            task3 = Task.objects.filter(name=task3_name,department=dept).first()

            if task1:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task1
                service.complete = True
                service.date = datetime.now()
                service.save()

            if task2:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task2
                service.complete = True
                service.date = datetime.now()
                service.save()

            if task3:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task3
                service.complete = True
                service.date = datetime.now()
                service.save()


            return HttpResponse("saved")
        return HttpResponse("not valid")

def inventory(request):
    if request.method =="GET":
        return render(request,"inventory.html")
    if request.method == "POST":
        service_name = request.POST["service"]

        user = request.user
        dept = user.userprofile.department
        task1_name = "Maintain Inventory" if request.POST.get("InventoryTask", " ") else""

        if dept.name == "Inventory":
            task1 = Task.objects.filter(name=task1_name,department=dept).first()

            if task1:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task1
                service.complete = True
                service.date = datetime.now()
                service.save()
            return HttpResponse("saved")
        return HttpResponse("not valid")



def truss(request):
    if request.method == "GET":
        return render(request, "truss.html")
    if request.method == "POST":
        service_name = request.POST["service"]

        user = request.user
        dept= user.userprofile.department
        task1_name ="Set Up The Truss" if request.POST.get("TrussTask", " ") else""

        if dept.name == "Truss":
            task1 = Task.objects.filter(name=task1_name,department=dept).first()

            if task1:
                service = Service()
                service.name = service_name
                service.user = user
                service.task = task1
                service.complete = True
                service.date = datetime.now()
                service.save()
            return HttpResponse("saved")
        return HttpResponse("not valid")


def temp(request):
    if request.method == "GET":

        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        # task = Task.objects.all()
        depts = Department.objects.all()
        for dept in depts:
            tasks = Task.objects.filter(department=dept)
            for task in tasks:
                services = Service.objects.filter(task=task, date__lte=today_end, date__gte=today_start)
                if services.exists():
                    if services.filter(name="morning", complete=True).exists():
                        dept.morning = "Done"
                    else:
                        dept.morning = "Incomplete"
                    if services.filter(name="afternoon", complete=True).exists():
                        dept.afternoon = "Done"
                    else:
                        dept.afternoon = "Incomplete"
                    if services.filter(name="evening", complete=True).exists():
                        dept.evening = "Done"
                    else:
                        dept.evening = "Incomplete"
                else:
                    dept.morning = "Incomplete"
                    dept.afternoon = "Incomplete"
                    dept.evening = "Incomplete"

        return render(request, "temp.html", {"departments": depts})


