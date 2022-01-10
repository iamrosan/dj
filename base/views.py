from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'base/index.html')

def pricing(request):
    return render(request,'base/pricing.html')
