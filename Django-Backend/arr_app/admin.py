from django.contrib import admin
from usermanagement.models import Waypoints
from arr_app.models import FrontWebsiteHero, FrontWebsitePartners, FrontWebsiteFeatures, FrontWebsiteVideo, FrontWebsiteInfo, FrontWebsitePricingSection, FrontWebsitePricingBoxes, FrontWebsiteCTA, FrontWebsiteInfoTitle

admin.site.register(Waypoints)

admin.site.register(FrontWebsiteHero)
admin.site.register(FrontWebsitePartners)
admin.site.register(FrontWebsiteFeatures)
admin.site.register(FrontWebsiteVideo)
admin.site.register(FrontWebsiteInfo)
admin.site.register(FrontWebsitePricingSection)
admin.site.register(FrontWebsitePricingBoxes)
admin.site.register(FrontWebsiteCTA)
admin.site.register(FrontWebsiteInfoTitle)

