from django.contrib import admin
from .models import (
    ProjectModel,
    HeroModel,
    AboutSectionModel,
    CommunityModel,
    ContactUsModel,
)

@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'giturl')
    search_fields = ('title', 'tech')


@admin.register(HeroModel)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'intro')


@admin.register(AboutSectionModel)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('bio', 'current_focus', 'hobbies')


@admin.register(CommunityModel)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('discord_url', 'linkedin_newletter', 'twitter')


@admin.register(ContactUsModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'linkedin', 'twitter')
