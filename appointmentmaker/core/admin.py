from django.contrib import admin

from core import models

admin.site.register(models.Appointee)
admin.site.register(models.Company)
admin.site.register(models.Appointment)