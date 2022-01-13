from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm



# Create your views here.

# ---------------without db--------------------
# rooms =[
#          {'id':1,'name':"Learn Python"},
#          {'id':2,'name':"Learn Javascript"},
#          {'id':3,'name':"Learn Data Science"}
#         ]
# ----------------------------------


def index(request):
    rooms = Room.objects.all #gets all the objects stored in our db
    context = {'rooms':rooms}
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
