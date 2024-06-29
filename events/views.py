from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

from .models import Event

# Create your views here.
def all_events(request):
    event_list =Event.objects.all()
    return render(request, 'events/event_list.html',{"event_list": event_list})



def home(request,year=datetime.now().year,month=datetime.now().strftime("%B")):
    month=month.capitalize()
    # conert month from name to number
    month_number =list(calendar.month_name).index(month)
    # convert to number
    month_number= int(month_number)
    cal =HTMLCalendar().formatmonth(year,month_number)
    now = datetime.now()
    current_year = now.year

    # time
    time = now.strftime('%I:%M:%S%p')

    return render(request,'events/home.html',{"cal":cal,"current_year":current_year,"time":time})

