from django.contrib import admin
from pollutionapp.models import User, Contact, Donate, WaterData

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Donate)
admin.site.register(WaterData)
