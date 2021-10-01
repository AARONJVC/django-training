from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Meeting, Room

# Create your views here.

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms(request):
    return  render(request, "meetings/rooms.html", {"rooms": Room.objects.all(), "count": Room.objects.count()})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new-meeting.html", {"form": form})

RoomForm = modelform_factory(Room, exclude=[])

def new_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rooms")
    else:
        form = RoomForm()
    return render(request, "meetings/new-room.html", {"form": form})