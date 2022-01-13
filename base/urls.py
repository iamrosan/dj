from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('pricing/',views.pricing, name='pricing'),
    path('rooms/<str:pk>',views.roomm, name='rooms'),
    path('create-room/', views.createRoom, name='create-room')

]