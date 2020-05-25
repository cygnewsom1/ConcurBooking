import string
from django.apps import AppConfig
from threading import Lock
import redis
from .settings import REDIS_SERVER_CONF


class RedisWrapper(object):
    shared_state = {}

    def __init__(self):
        self.__dict__ = self.shared_state

    def redis_connect(self, server_key):
        redis_server_conf = REDIS_SERVER_CONF['servers'][server_key]
        connection_pool = redis.ConnectionPool(host=redis_server_conf['HOST'], port=redis_server_conf['PORT'],
                                               db=redis_server_conf['DATABASE'])
        return redis.StrictRedis(connection_pool=connection_pool)


class ConcurBookingConfig(AppConfig):
    name = 'ConcurBooking'
    quantity_lock = Lock()
    redis_conn = RedisWrapper().redis_connect(server_key='main_server')
    quantity = int(redis_conn.get('quantity_per_node'))
