from django.shortcuts import render
import calendar
from calendar import HTMLCalendar


# Create your views here.
def home(request, year, month):
    mont_num = int(list(calendar.month_name).index(month.capitalize()))
    html_cal = HTMLCalendar().formatmonth(year, mont_num)

    return render(request, "fronts/home.html", {"html_cal": html_cal})
