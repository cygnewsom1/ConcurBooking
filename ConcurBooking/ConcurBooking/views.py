from django.http import HttpResponse
from .app import ConcurBookingConfig as cbc
import logging

logger = logging.getLogger(__name__)


def detail(request):
    cbc.quantity_lock.acquire()
    redis_quantity = cbc.redis_conn.get('quantity')
    #print("{} {}".format(cbc.quantity, redis_quantity))
    if cbc.quantity > 0 and int(redis_quantity) > 0:
        cbc.quantity -= 1
        cbc.redis_conn.decr('quantity', 1)
        cbc.quantity_lock.release()
        logger.info("{} {}".format(cbc.quantity, redis_quantity))
        return HttpResponse("Congratulations, you got an item")
    else:
        cbc.quantity_lock.release()
        return HttpResponse("Sorry the item is soldout")
