from django.db import models
from django.contrib import admin
class bike_servise(models.Model):
    bike_no=models.CharField(primary_key=True)
    company_name=models.CharField(max_length=30)
    owner_name=models.CharField(max_length=20)
    service_date=models.IntegerField()
    problem=models.CharField()
    bike_no=models.CharField()
    phon_no=models.IntegerField()
    manufacturing_year=models.IntegerField()
class bike_servise_Admin(admin.ModelAdmin):
    list_display=("bike_no","company_name","phon_no","manufacturing_year","problem","owner_name","service_date")


