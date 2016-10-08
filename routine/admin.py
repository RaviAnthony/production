from django.contrib import admin
from .models import Department,UserProfile,Task,Service

admin.site.register(Department)
admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(Service)
