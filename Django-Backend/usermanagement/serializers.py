from django.apps import apps
UserLocation = apps.get_model('usermanagement', 'UserLocation')
from rest_framework import serializers

class UserLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLocation
        ul_user = serializers.CurrentUserDefault()
        fields = ('ul_user', 'ul_location_lat', 'ul_location_lng')


