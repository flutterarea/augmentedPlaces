from django.db import models

class FrontWebsiteHero(models.Model):
    fwh_id = models.AutoField(primary_key=True)
    fwh_hero_title = models.CharField(max_length=255)
    fwh_hero_subtitle = models.TextField()
    fwh_hero_btn_text = models.CharField(max_length=255)
    fwh_hero_btn_url = models.CharField(max_length=255)
    fwh_hero_banner_image = models.CharField(max_length=255)

    def __str__(self):
        return self.fwh_hero_title

    class Meta:
        # managed = False
        db_table = 'front_website_hero'

    
class FrontWebsitePartners(models.Model):
    fwp_id = models.AutoField(primary_key=True)
    fwp_partner_image = models.CharField(max_length=255)
    fwp_partner_url = models.CharField(max_length=255)

    def __str__(self):
        return self.fwp_partner_url

    class Meta:
        # managed = False
        db_table = 'front_website_partners'



class FrontWebsiteFeatures(models.Model):
    fwf_id = models.AutoField(primary_key=True)
    fwf_features_title = models.CharField(max_length=255)
    fwf_features_description = models.TextField()
    fwf_features_image = models.CharField(max_length=255)

    def __str__(self):
        return self.fwf_features_title

    class Meta:
        # managed = False
        db_table = 'front_website_features'



class FrontWebsiteVideo(models.Model):
    fwv_id = models.AutoField(primary_key=True)
    fwv_video_title = models.CharField(max_length=255)
    fwv_video_url = models.CharField(max_length=255)
    fwv_video_cover = models.CharField(max_length=255)

    def __str__(self):
        return self.fwv_video_title

    class Meta:
        # managed = False
        db_table = 'front_website_video'



class FrontWebsiteInfo(models.Model):
    fwi_id = models.AutoField(primary_key=True)
    fwi_info_title = models.CharField(max_length=255)
    fwi_info_description = models.TextField()
    fwi_info_banner_image = models.CharField(max_length=255)

    def __str__(self):
        return self.fwi_info_title

    class Meta:
        # managed = False
        db_table = 'front_website_info'



class FrontWebsitePricingSection(models.Model):
    fwps_id = models.AutoField(primary_key=True)
    fwps_pricing_section_title = models.CharField(max_length=255)
    fwps_pricing_section_description = models.TextField()
    fwps_pricing_section_bottom = models.TextField()

    def __str__(self):
        return self.fwps_pricing_section_title

    class Meta:
        # managed = False
        db_table = 'front_website_pricing_section'


class FrontWebsiteInfoTitle(models.Model):
    fwit_id = models.AutoField(primary_key=True)
    fwit_title = models.CharField(max_length=255)
    fwit_description = models.TextField()

    def __str__(self):
        return self.fwit_title

    class Meta:
        # managed = False
        db_table = 'front_website_info_title'


class FrontWebsitePricingBoxes(models.Model):
    fwpb_id = models.AutoField(primary_key=True)
    fwpb_pricing_boxes_title = models.CharField(max_length=255)
    fwpb_pricing_boxes_price_month = models.FloatField(blank=True, null=True)
    fwpb_pricing_boxes_price_year = models.FloatField(blank=True, null=True)
    fwpb_pricing_boxes_f1 = models.CharField(max_length=255)
    fwpb_pricing_boxes_f1_active = models.BooleanField()
    fwpb_pricing_boxes_f2 = models.CharField(max_length=255)
    fwpb_pricing_boxes_f2_active = models.BooleanField()
    fwpb_pricing_boxes_f3 = models.CharField(max_length=255)
    fwpb_pricing_boxes_f3_active = models.BooleanField()
    fwpb_pricing_boxes_f4 = models.CharField(max_length=255)
    fwpb_pricing_boxes_f4_active = models.BooleanField()
    fwpb_pricing_boxes_f5 = models.CharField(max_length=255)
    fwpb_pricing_boxes_f5_active = models.BooleanField()

    def __str__(self):
        return self.fwpb_pricing_boxes_title

    class Meta:
        # managed = False
        db_table = 'front_website_pricing_boxes'


class FrontWebsiteCTA(models.Model):
    fwcta_id = models.AutoField(primary_key=True)
    fwcta_cta_title = models.CharField(max_length=255)
    fwcta_cta_btn_text = models.CharField(max_length=255)
    fwcta_cta_btn_url = models.CharField(max_length=255)

    def __str__(self):
        return self.fwcta_cta_title

    class Meta:
        # managed = False
        db_table = 'front_website_pricing_cta'