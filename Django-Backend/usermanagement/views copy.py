from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import WaypointForm
from datetime import datetime
from .models import Waypoints, UserLocation
from .serializers import UserLocationSerializer
from rest_framework import viewsets

@login_required(login_url='login')
def dash(request):
    user = request.user
    wps = Waypoints.objects.filter(waypoint_user=user)
    
    if request.method == "POST":
        form = WaypointForm(request.POST)
        if form.is_valid():
            wp = form.save(commit=False)
            wp.waypoint_user = request.user
            wp.waypoint_added = datetime.now()
            wp.save()
            return redirect('/users/dash/')
    else:
        form = WaypointForm()
    return render(request, 'dash.html', {'wps': wps, 'form': form})


class UserLocationViewSet(viewsets.ModelViewSet):
    serializer_class = UserLocationSerializer

    def get_queryset(self, *args, **kwargs):
        return UserLocation.objects.all().filter(ul_user=self.request.user)


class UserLocationViewSetDetails(viewsets.ModelViewSet):
    serializer_class = UserLocationSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

