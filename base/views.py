from django.shortcuts import render

# Create your views here.

rooms =[
         {'id':1,'name':"Learn Python"},
         {'id':2,'name':"Learn Javascript"},
         {'id':3,'name':"Learn Data Science"}
        ]



def index(request):
    context = {'rooms':rooms}
    return render(request,'base/index.html',context)

def pricing(request):
    return render(request,'base/pricing.html')

def room(request,pk):
    room =None
    for i in rooms:
        if(i['id'] == int(pk)):
            room=i
    context = {'room':room}
    return render(request,'base/rooms.html',context)