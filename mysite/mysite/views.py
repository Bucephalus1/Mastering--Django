from django.http import HttpResponse,Http404
import datetime

def hello(request):
    return HttpResponse("hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now {!s}".format(now)
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = 'In {!s} hour(s), it will be {!s}.'.format(offset,dt)
    return HttpResponse(html)
