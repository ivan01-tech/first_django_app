from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime


def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    cap_monht = month.capitalize()
    mont_num = int(list(calendar.month_name).index(cap_monht))
    html_cal = HTMLCalendar().formatmonth(year, mont_num)

    return render(request, "events/home.html", {"html_cal": html_cal})
