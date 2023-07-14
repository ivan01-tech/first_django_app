from django.contrib import admin
import django.db
from .models import Event, MyClubsUser, Venue

# admin.site.register(Venue)
admin.site.register(MyClubsUser)
admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name','address',"phone")
    ordering = ("name",)
    # ordering = ("-name",)
    search_fields = ("name","adress",)
    
# admin.site.register(Venue, VenueAdmin)
