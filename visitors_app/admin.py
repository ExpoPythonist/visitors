from django.contrib import admin
from visitors_app import models

# Register your models here.
admin.site.register(models.Departments)
admin.site.register(models.Visitors)
