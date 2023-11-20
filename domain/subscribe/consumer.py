#!/usr/bin/env python
import threading
from domain.messageMQ.rabbitmq import rabbitmq
from . import config


class consumer(rabbitmq):

    def __init__(self, queue_name=''):
        super().__init__()
        self._queue_name = self.queue_declare(queue=queue_name)
        self.queue_bind(exchange=config.EXCHANGE, queue=self._queue_name)

    def basic_consume(self):
        print(' [*] Waiting for logs. To exit press CTRL+C')
        threading.Thread(target=super().basic_consume,
                         args=(self._queue_name, self.callback, True,)).start()

    def callback(self, ch, method, properties, body):
        print("consumer: {}".format(body.decode()))

    @classmethod
    def new_consumer(cls) -> 'consumer':
        return cls()
