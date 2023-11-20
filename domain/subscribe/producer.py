#!/usr/bin/env python
import threading
from domain.messageMQ.rabbitmq import rabbitmq
from . import config


class producer(rabbitmq):

    def __init__(self):
        super().__init__()

    def basic_publish(self, body=''):
        threading.Thread(target=super().basic_publish,
                         args=(config.EXCHANGE, '', body,)).start()

    @classmethod
    def new_producer(cls) -> 'producer':
        return cls()
