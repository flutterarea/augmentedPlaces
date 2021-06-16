from django.shortcuts import render
from math import *
from .models import FrontWebsiteHero, FrontWebsitePartners, FrontWebsiteFeatures, FrontWebsiteVideo, FrontWebsiteInfo, FrontWebsitePricingSection, FrontWebsitePricingBoxes, FrontWebsiteCTA, FrontWebsiteInfoTitle
from django.apps import apps
Waypoints = apps.get_model('usermanagement', 'Waypoints')


def home(request):
    fwh = FrontWebsiteHero.objects.all()
    fwp = FrontWebsitePartners.objects.all()
    fwf = FrontWebsiteFeatures.objects.all()
    fwv = FrontWebsiteVideo.objects.all()
    fwi = FrontWebsiteInfo.objects.all()
    fwps = FrontWebsitePricingSection.objects.all()
    fwpb = FrontWebsitePricingBoxes.objects.all()
    fwcta = FrontWebsiteCTA.objects.all()
    fwit = FrontWebsiteInfoTitle.objects.all()


    return render(request, 'home.html', {
        'fwh': fwh,
        'fwp': fwp,
        'fwf': fwf,
        'fwv': fwv,
        'fwi': fwi,
        'fwps': fwps,
        'fwpb': fwpb,
        'fwcta': fwcta,
        'fwit': fwit,
        })

RADIUS = 6371 #Earth's raadius in km

def distance(origin, destiny):
    (latitude1, longitude1) = (origin[0], origin[1])
    (latitude2, longitude2) = (destiny[0], destiny[1])

    dLat = radians(latitude1 - latitude2)
    dLong = radians(longitude1 - longitude2)

    a = sin(dLat/2) * sin(dLat/2) + cos(radians(latitude1)) * cos(radians(latitude2)) * sin(dLong/2) * sin(dLong/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return (RADIUS * c)

# a test
origin = (40.96312364002175, -5.661885738372803)



def demo(request):
    wps = Waypoints.objects.all()
    return render(request, 'demo.html', {'wps': wps})

def join(request):
    wps = Waypoints.objects.all()
    for wp in wps:
        destiny = (float(wp.waypoint_coords_lat), float(wp.waypoint_coords_lng))
        wp.distance = distance(origin, destiny);
    return render(request, 'join.html', {'wps': wps})

def profile(request):
    return render(request, 'home.html', {})
