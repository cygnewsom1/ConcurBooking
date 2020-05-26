import string
from django.apps import AppConfig
from threading import Lock
import threading
import redis
from .settings import REDIS_SERVER_CONF


class RedisWrapper(object):
    shared_state = {}

    def __init__(self):
        self.__dict__ = self.shared_state

    def redis_connect(self, server_key):
        redis_server_conf = REDIS_SERVER_CONF['servers'][server_key]
        connection_pool = redis.ConnectionPool(host=redis_server_conf['HOST'], port=redis_server_conf['PORT'],
                                               db=redis_server_conf['DATABASE'], max_connections=redis_server_conf['MAX_CONNECTIONS'])
        return redis.StrictRedis(connection_pool=connection_pool)


class Item:
    def __init__(self, item_id, item_quantity):
        self._item_id = item_id
        self._item_quantity = item_quantity
        self.lock = Lock()

    def decr(self):
        with self.lock:
            redis_quantity = ConcurBookingConfig.redis_conn.get('quantity')
            print("{} {} {}".format(self._item_quantity, redis_quantity, threading.current_thread().name))
            if self._item_quantity > 0 and int(redis_quantity) > 0:
                self._item_quantity -= 1
                ConcurBookingConfig.redis_conn.decr('quantity', 1)
                return True
            else:
                return False
    @property
    def item_quantity(self):
        return self._item_quantity


class ConcurBookingConfig(AppConfig):
    name = 'ConcurBooking'
    quantity_lock = Lock()
    redis_conn = RedisWrapper().redis_connect(server_key='main_server')
    quantity = int(redis_conn.get('quantity'))
    item = Item('default_item', quantity)
