from django.contrib import admin
from .models import Profile,Location

class profileAdmin(admin.ModelAdmin):
    pass

class locationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, profileAdmin)
admin.site.register(Location, locationAdmin)
