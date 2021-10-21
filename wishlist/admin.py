from django.contrib import admin

# Register your models here.
from .models import AdminUsers, Users

admin.site.register(AdminUsers, Users)
