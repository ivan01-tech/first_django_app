from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import VenueForm
from django.http import HttpResponseRedirect


def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    cap_monht = month.capitalize()
    mont_num = int(list(calendar.month_name).index(cap_monht))
    html_cal = HTMLCalendar().formatmonth(year, mont_num)

    return render(request, "events/home.html", {"html_cal": html_cal})


def add_venue(request):
    submitted = False
    if request.methpd == "POST":
        venue_form = VenueForm(request.POST)
        if venue_form.is_valid():
            venue_form.save()
            return HttpResponseRedirect(
                "/add-venue?submitted=True",
            )
        # else: 
        #     return HttpResponseRedirect(
        #         "/add-venue",
        #     )
    else: 
        venue_form = VenueForm
        if "submitted" in request.GET:
            