from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.rooms, name="rooms"),
    path('new-meeting', views.new_meeting, name="new meeting"),
    path('new-room', views.new_room, name="new room"),
]