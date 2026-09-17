from django.contrib import admin
from .models import House, City


admin.site.register((House, City))
