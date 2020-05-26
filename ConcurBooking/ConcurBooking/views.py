from django.http import HttpResponse
from .app import ConcurBookingConfig as cbc
import logging

logger = logging.getLogger(__name__)


def detail(request):
    if cbc.item.decr():
        return HttpResponse("Congratulations, you got an item")
    else:
        return HttpResponse("Sorry the item is soldout")
