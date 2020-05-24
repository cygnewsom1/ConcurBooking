from django.http import HttpResponse
import threading
from .app import ConcurBookingConfig as cbc
import logging

logger = logging.getLogger(__name__)

def detail(request):
    cbc.quantity_lock.acquire()
    ret = cbc.redis_connect.ping()
    print(ret)
    if cbc.quantity > 0:
        cbc.quantity -= 1

    cbc.quantity_lock.release()
    logger.info("{} {} {}".format(threading.active_count(), threading.current_thread().name, cbc.quantity))
    return HttpResponse("Hello {} {} {}".format(threading.active_count(), threading.current_thread().name, cbc.quantity))
