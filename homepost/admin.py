from django.contrib import admin

# Register your models here.

from homepost.models import Posts

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posts, AuthorAdmin)