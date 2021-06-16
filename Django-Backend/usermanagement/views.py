from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import WaypointForm, UserLocationForm
from datetime import datetime
from .models import Waypoints, UserLocation
from .serializers import UserLocationSerializer
from rest_framework import viewsets
from django.http import HttpResponse


@login_required(login_url='login')
def dash(request):
    user = request.user
    wps = Waypoints.objects.filter(waypoint_user=user)
    locations = UserLocation.objects.all()
    
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
    return render(request, 'dash.html', {'wps': wps, 'form': form, 'locations': locations})




from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = UserLocation.objects.all()
        serializer = UserLocationSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        pass





@login_required(redirect_field_name=None, login_url='login')
def update_location(request):

    lat = request.POST.get('lat', False)
    lng = request.POST.get('lng', False)

    try:
        obj = UserLocation.objects.filter(ul_user=request.user).update(
            ul_user = request.user.id,
            ul_location_lat = lat,
            ul_location_lng = lng
        )
        obj.save()

        # Setting output
        response = {
            'status': 1,
            'message': 'Game saved'
        }
    except Exception as e:

         # Something went wrong
         response = {
             'status': 0,
             'message': 'Something went wrong - ' +str(e) 
         }

    return HttpResponse(response)