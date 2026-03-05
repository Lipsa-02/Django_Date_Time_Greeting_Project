from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def date_time_info(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='<h1>Hello Guest Very '
    if h<12:
        msg+='Good Morning'
    elif h>=12 and h<17:
        msg+= 'Good Afternoon'
    elif h >= 17 and h < 21:
        msg+='Good Evening'
    else:
        msg+='Good Night'
    msg+='</h1><hr>'
    msg+='<h1>Now server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)

