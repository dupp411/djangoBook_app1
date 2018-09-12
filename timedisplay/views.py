from django.http import HttpResponse
from datetime import datetime, timedelta
# Create your views here.

def current_time(request):
    now = datetime.now()
    html = "<html><body>Current datetime is: %s </body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, hour_diff):
    hour_diff = int(hour_diff)
    future_time = datetime.now() + timedelta(hours = hour_diff)
    html = "<html><body>In %s hours the datetime will be %s" % (hour_diff, future_time)
    return HttpResponse(html)                                           