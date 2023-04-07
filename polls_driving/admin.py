from django.contrib import admin
from .models import RoleUser, Users, Planning

# Register your models here.
admin.site.register(Planning)
admin.site.register(RoleUser)
admin.site.register(Users)

