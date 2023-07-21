from django.contrib import admin
import django.db
from .models import Event, MyClubsUser, Venue
# this helps to personalyse django admin interface
#email backend... conf
#novalidate attr form
# error form

# admin.site.register(Venue)
admin.site.register(MyClubsUser)
# admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone", )
    ordering = ("name",)
    # ordering = ("-name",)
    search_fields = (
        "name",
        "adress",
    )


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "venue", "event_date","manager",)
    ordering = ("-event_date",)
    fields = (("name", "venue"), "event_date",)
    list_filter = ("event_date", "venue",)


admin.site.register(Event, EventAdmin)
# admin.site.register(Venue, VenueAdmin)
