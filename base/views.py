from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q
# from django.conf import settings


from django.contrib import messages


# Create your views here.

# ---------------without db--------------------
# rooms =[
#          {'id':1,'name':"Learn Python"},
#          {'id':2,'name':"Learn Javascript"},
#          {'id':3,'name':"Learn Data Science"}
#         ]
# ----------------------------------

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.error(request, 'User not available')
            
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,'Username or password is incorrect')
            return redirect('login')

    # context ={}
    else:
        return render(request, 'base/login_Register.html')

def loogout(request):
    logout(request)
    return redirect('index')


def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    # rooms = Room.objects.all #gets all the objects stored in our db
    
    rooms = Room.objects.filter(    #Search functionality wth of topic username and description
        Q(topic__name__icontains= q) |
        Q(name__icontains= q) |
        Q(description__icontains= q) | 
        Q(host__username__icontains= q) 
        )
    topics = Topic.objects.all
    room_count = rooms.count()
    context = {'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request,'base/index.html',context)

def pricing(request):
    return render(request,'base/pricing.html')

def roomm(request,pk):
    # room =None
    # for i in rooms:
    #     if(i['id'] == int(pk)):
    #         room=i
    room = Room.objects.get(id=pk)  #get le unique obj return garxa so we passed primary key pk as unique value to get
    context = {'room':room}
    return render(request,'base/rooms.html',context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context ={'form':form}
    return render(request,'base/createRoom.html',context)


def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'base/update_room.html',context)



def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('index')
    
    context={'room':room}
    return render(request, 'base/delete_Room.html', context)