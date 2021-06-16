from django import forms
from .models import Waypoints, UserLocation

class WaypointForm(forms.ModelForm):

    class Meta:
        model = Waypoints
        fields = ('waypoint_name',
        'waypoint_coords_lat',
        'waypoint_coords_lng',
        'waypoint_url',
        'waypoint_description',
        'waypoint_logo',
        'waypoint_address'
         ) 

class UserLocationForm(forms.ModelForm):

    class Meta:
        model = UserLocation
        fields = ('ul_user',
        'ul_location_lat',
        'ul_location_lng',
         ) 