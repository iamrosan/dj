from django.urls import path
from . import views

urlpatterns =[
    path('login/',views.loginPage, name='login'),
    path('logout/',views.loogout, name='logout'),
    path('',views.index,name='index'),
    path('pricing/',views.pricing, name='pricing'),
    path('rooms/<str:pk>',views.roomm, name='rooms'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),

]