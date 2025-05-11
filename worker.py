from os import getenv

import gevent
from gevent.exceptions import GreenletExit
from gunicorn.workers.ggevent import GeventWorker


class CustomGeventWorker(GeventWorker):
    def handle_request(self, listener_name, req, sock, addr):
        try:
            with gevent.Timeout(getenv('REQUEST_TIMEOUT', default=30)):
                super().handle_request(listener_name, req, sock, addr)
        except gevent.Timeout:
            raise GreenletExit
