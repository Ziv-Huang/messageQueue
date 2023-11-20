import pika
from domain.subscribe import config

class rabbitmq():

    def __init__(self):
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        self.exchange_declare()

    def exchange_declare(self, exchange=config.EXCHANGE,
                         exchange_type='fanout', passive=True):
        self._channel.exchange_declare(exchange=exchange,
                                       exchange_type=exchange_type,
                                       passive=passive)

    def queue_declare(self, queue=''):
        result = self._channel.queue_declare(queue=queue, exclusive=True)
        return result.method.queue

    def queue_bind(self, exchange=config.EXCHANGE, queue='', routing_key=''):
        self._channel.queue_bind(exchange=exchange, queue=queue,
                                 routing_key=routing_key)

    def basic_publish(self, exchange=config.EXCHANGE, routing_key='', body=''):
        self._channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body)

    def basic_consume(self, queue='', on_message_callback=None, auto_ack=True):
        self._channel.basic_consume(
            queue=queue, on_message_callback=on_message_callback, auto_ack=auto_ack)
        self.start_consuming()

    def start_consuming(self):
        print("start consuming")
        self._channel.start_consuming()

    def close(self):
        self._channel.close()
        self._connection.close()
