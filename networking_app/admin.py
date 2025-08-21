from django.contrib import admin
from .models import NetworkingUserModel
# Register your models here.
@admin.register(NetworkingUserModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id','designation')
    search_fields = ('name', 'designation')