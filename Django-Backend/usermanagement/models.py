from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Waypoints(models.Model):
    waypoint_id = models.AutoField(primary_key=True)
    waypoint_name = models.CharField(max_length=255)
    waypoint_description = models.TextField()
    waypoint_logo = models.CharField(max_length=255)
    waypoint_address = models.TextField()
    waypoint_coords_lat = models.CharField(max_length=24)
    waypoint_coords_lng = models.CharField(max_length=24)
    waypoint_added = models.DateTimeField()
    waypoint_url = models.CharField(max_length=255)
    waypoint_user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.waypoint_name

    class Meta:
        # managed = False
        db_table = 'waypoints'

class UserLocation(models.Model):
    ul_user = models.OneToOneField(User, on_delete=models.CASCADE)
    ul_location_lat = models.FloatField(blank=False, null=False)
    ul_location_lng = models.FloatField(blank=False, null=False)

    def __str__(self):
      return self.ul_user.username

class UserProfile(models.Model):
    upr_user = models.OneToOneField(User, on_delete=models.CASCADE)
    upr_package = models.IntegerField(blank=False, null=False)

    def __str__(self):
      return self.upr_user.username

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        up = UserLocation(ul_user=user, ul_location_lat=0.0, ul_location_lng=0.0)
        up.save()
        upr = UserProfile(up_user=user, upr_package=0)
        upr.save()
post_save.connect(create_profile, sender=User)

