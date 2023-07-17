from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Venue
from .forms import VenueForm
from django.http import HttpResponseRedirect


def list_venue(request):
    venues = Venue.objects.all()
    return render(request, "events/venue_list.html", {"venues": venues})


def search(request):
    if request.method == "POST":
        search_term = request.POST["search"]
        venues = Venue.objects.filter(name__contains=search_term)
        print("venues : ",venues)
    return render(
        request, "events/search.html", {"venues": venues, "search_term": search_term}
    )


def venue_item(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    return render(request, "events/venue_item.html", {"venue": venue})


def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    cap_monht = month.capitalize()
    mont_num = int(list(calendar.month_name).index(cap_monht))
    html_cal = HTMLCalendar().formatmonth(year, mont_num)

    return render(request, "events/home.html", {"html_cal": html_cal})


def add_venue(request):
    submitted = False
    if request.method == "POST":
        submitted = False
        venue_form = VenueForm(request.POST)
        if venue_form.is_valid():
            venue_form.save()
            return HttpResponseRedirect(
                "/events/add_venue?submitted=True",
            )
    else:
        venue_form = VenueForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request, "events/add_venue.html", {"submitted": True, "form": venue_form}
    )
