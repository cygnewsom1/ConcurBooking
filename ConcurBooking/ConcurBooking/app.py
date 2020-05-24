import string

from django.apps import AppConfig
from threading import Lock
import redis

REDIS_SERVER_CONF = {
    'servers': {
        'main_server': dict(HOST='127.0.0.1', PORT=6379, DATABASE=0)
    }
}


class RedisWrapper(object):
    shared_state = {}

    def __init__(self):
        self.__dict__ = self.shared_state

    def redis_connect(self, server_key: string) -> redis.client:
        redis_server_conf = REDIS_SERVER_CONF['servers'][server_key]
        connection_pool = redis.ConnectionPool(host=redis_server_conf['HOST'], port=redis_server_conf['PORT'],
                                               db=redis_server_conf['DATABASE'])
        return redis.StrictRedis(connection_pool=connection_pool)


class ConcurBookingConfig(AppConfig):
    name = 'ConcurBooking'
    quantity = 50
    quantity_lock = Lock()
    redis_connect = RedisWrapper.redis_connect(server_key='main server')
